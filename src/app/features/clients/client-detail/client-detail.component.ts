import { ChangeDetectionStrategy, Component, inject, signal } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { ClientService } from '../../../core/services/client.service';
import { AddressService } from '../../../core/services/address.service';
import { CleaningServiceService } from '../../../core/services/cleaning-service.service';
import { Client } from '../../../core/models/client.model';
import { Address } from '../../../core/models/address.model';
import { CleaningService } from '../../../core/models/cleaning-service.model';
import { daysUntil, getAlertLevel } from '../../../core/utils/alert.util';
import { formatDate } from '../../../core/utils/date.util';

interface AddressWithServices {
  address: Address;
  services: CleaningService[];
}

@Component({
  selector: 'app-client-detail',
  imports: [RouterLink, ReactiveFormsModule],
  templateUrl: './client-detail.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ClientDetailComponent {
  private readonly route = inject(ActivatedRoute);
  private readonly clientService = inject(ClientService);
  private readonly addressService = inject(AddressService);
  private readonly cleaningServiceService = inject(CleaningServiceService);
  private readonly formBuilder = inject(FormBuilder);

  private readonly clientId = this.route.snapshot.paramMap.get('id')!;

  protected readonly client = signal<Client | null>(null);
  protected readonly addresses = signal<AddressWithServices[]>([]);
  protected readonly openServiceFormFor = signal<string | null>(null);

  protected readonly addressForm = this.formBuilder.nonNullable.group({
    label: ['', Validators.required],
    street: ['', Validators.required],
    city: [''],
  });

  protected readonly serviceForm = this.formBuilder.nonNullable.group({
    type: ['Limpeza de painel solar', Validators.required],
    performedAt: [new Date().toISOString().slice(0, 10), Validators.required],
    intervalDays: [180, [Validators.required, Validators.min(1)]],
  });

  protected readonly formatDate = formatDate;
  protected readonly alertLevelOf = getAlertLevel;
  protected readonly daysUntilOf = daysUntil;

  constructor() {
    this.loadClient();
    this.loadAddresses();
  }

  protected addAddress(): void {
    if (this.addressForm.invalid) {
      return;
    }

    const { label, street, city } = this.addressForm.getRawValue();
    this.addressService.create(this.clientId, { label, street, city: city || undefined }).subscribe((address) => {
      this.addresses.update((current) => [...current, { address, services: [] }]);
      this.addressForm.reset();
    });
  }

  protected removeAddress(address: Address): void {
    if (!confirm(`Excluir ${address.label}?`)) {
      return;
    }

    this.addressService.delete(address.id).subscribe(() => {
      this.addresses.update((current) => current.filter((entry) => entry.address.id !== address.id));
    });
  }

  protected toggleServiceForm(addressId: string): void {
    this.openServiceFormFor.update((current) => (current === addressId ? null : addressId));
    this.serviceForm.reset({
      type: 'Limpeza de painel solar',
      performedAt: new Date().toISOString().slice(0, 10),
      intervalDays: 180,
    });
  }

  protected addService(addressId: string): void {
    if (this.serviceForm.invalid) {
      return;
    }

    const { type, performedAt, intervalDays } = this.serviceForm.getRawValue();
    this.cleaningServiceService
      .create(addressId, { type, performedAt: new Date(performedAt).toISOString(), intervalDays })
      .subscribe((service) => {
        this.addresses.update((current) =>
          current.map((entry) =>
            entry.address.id === addressId ? { ...entry, services: [service, ...entry.services] } : entry,
          ),
        );
        this.openServiceFormFor.set(null);
      });
  }

  protected removeService(addressId: string, service: CleaningService): void {
    this.cleaningServiceService.delete(service.id).subscribe(() => {
      this.addresses.update((current) =>
        current.map((entry) =>
          entry.address.id === addressId
            ? { ...entry, services: entry.services.filter((s) => s.id !== service.id) }
            : entry,
        ),
      );
    });
  }

  private loadClient(): void {
    this.clientService.getById(this.clientId).subscribe((client) => this.client.set(client));
  }

  private loadAddresses(): void {
    this.addressService.getByClient(this.clientId).subscribe((addresses) => {
      this.addresses.set(addresses.map((address) => ({ address, services: [] })));
      addresses.forEach((address) => this.loadServices(address.id));
    });
  }

  private loadServices(addressId: string): void {
    this.cleaningServiceService.getByAddress(addressId).subscribe((services) => {
      this.addresses.update((current) =>
        current.map((entry) => (entry.address.id === addressId ? { ...entry, services } : entry)),
      );
    });
  }
}
