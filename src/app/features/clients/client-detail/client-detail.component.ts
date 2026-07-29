import { ChangeDetectionStrategy, Component, inject, signal } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { ClientService } from '../../../core/services/client.service';
import { AddressService } from '../../../core/services/address.service';
import { WorkOrderService } from '../../../core/services/work-order.service';
import { Client } from '../../../core/models/client.model';
import { Address } from '../../../core/models/address.model';
import { WORK_ORDER_TYPE_LABELS, WORK_ORDER_TYPES, WorkOrder, WorkOrderType } from '../../../core/models/work-order.model';
import { daysUntilNext, getAlertLevel } from '../../../core/utils/alert.util';
import { formatDate } from '../../../core/utils/date.util';

interface AddressWithWorkOrders {
  address: Address;
  workOrders: WorkOrder[];
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
  private readonly workOrderService = inject(WorkOrderService);
  private readonly formBuilder = inject(FormBuilder);

  private readonly clientId = this.route.snapshot.paramMap.get('id')!;

  protected readonly workOrderTypes = WORK_ORDER_TYPES;
  protected readonly workOrderTypeLabels = WORK_ORDER_TYPE_LABELS;  

  protected readonly client = signal<Client | null>(null);
  protected readonly addresses = signal<AddressWithWorkOrders[]>([]);
  protected readonly openWorkOrderFormFor = signal<string | null>(null);

  protected readonly addressForm = this.formBuilder.nonNullable.group({
    label: ['', Validators.required],
    street: ['', Validators.required],
    city: [''],
  });

  protected readonly workOrderForm = this.formBuilder.nonNullable.group({
    type: ['CleaningJob' as WorkOrderType, Validators.required],
    date: [new Date().toISOString().slice(0, 10), Validators.required],
    price: [null as number | null],
    quantity: [null as number | null],
    description: [''],
  });

  protected readonly formatDate = formatDate;
  protected readonly alertLevelOf = getAlertLevel;
  protected readonly daysUntilOf = daysUntilNext;

  constructor() {
    this.loadClient();
    this.loadAddresses();
  }

  protected addAddress(): void {
    if (this.addressForm.invalid) {
      return;
    }

    const { label, street, city } = this.addressForm.getRawValue();
    this.addressService.create(this.clientId, { label: label || undefined, street: street || undefined, city }).subscribe((address) => {
      this.addresses.update((current) => [...current, { address, workOrders: [] }]);
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

  protected toggleWorkOrderForm(addressId: string): void {
    this.openWorkOrderFormFor.update((current) => (current === addressId ? null : addressId));
    this.workOrderForm.reset({
      type: 'CleaningJob',
      date: new Date().toISOString().slice(0, 10),
      price: null,
      quantity: null,
      description: '',
    });
  }

  protected addWorkOrder(addressId: string): void {
    if (this.workOrderForm.invalid) {
      return;
    }

    const { type, date, price, quantity, description } = this.workOrderForm.getRawValue();
    this.workOrderService
      .create(addressId, { type, date: new Date(date).toISOString(), price, quantity, description })
      .subscribe((workOrder) => {
        this.addresses.update((current) =>
          current.map((entry) =>
            entry.address.id === addressId
              ? { ...entry, workOrders: [workOrder, ...entry.workOrders] }
              : entry,
          ),
        );
        this.openWorkOrderFormFor.set(null);
      });
  }

  protected removeWorkOrder(addressId: string, workOrder: WorkOrder): void {
    this.workOrderService.delete(workOrder.id).subscribe(() => {
      this.addresses.update((current) =>
        current.map((entry) =>
          entry.address.id === addressId
            ? { ...entry, workOrders: entry.workOrders.filter((w) => w.id !== workOrder.id) }
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
      this.addresses.set(addresses.map((address) => ({ address, workOrders: [] })));
      addresses.forEach((address) => this.loadWorkOrders(address.id));
    });
  }

  private loadWorkOrders(addressId: string): void {
    this.workOrderService.getByAddress(addressId).subscribe((workOrders) => {
      this.addresses.update((current) =>
        current.map((entry) => (entry.address.id === addressId ? { ...entry, workOrders } : entry)),
      );
    });
  }
}