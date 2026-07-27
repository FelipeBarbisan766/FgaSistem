import { ChangeDetectionStrategy, Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { ClientService } from '../../../core/services/client.service';
import { Client } from '../../../core/models/client.model';

@Component({
  selector: 'app-client-list',
  imports: [RouterLink, ReactiveFormsModule],
  templateUrl: './client-list.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ClientListComponent {
  private readonly clientService = inject(ClientService);
  private readonly formBuilder = inject(FormBuilder);

  protected readonly clients = signal<Client[]>([]);

  protected readonly form = this.formBuilder.nonNullable.group({
    name: ['', Validators.required],
    email: [''],
    phone: [''],
  });

  constructor() {
    this.loadClients();
  }

  protected submit(): void {
    if (this.form.invalid) {
      return;
    }

    const { name, email, phone } = this.form.getRawValue();
    this.clientService
      .create({ name, email: email || undefined, phone: phone || undefined })
      .subscribe((client) => {
        this.clients.update((current) => [...current, client]);
        this.form.reset();
      });
  }

  protected removeClient(client: Client): void {
    if (!confirm(`Excluir ${client.name}?`)) {
      return;
    }

    this.clientService.delete(client.id).subscribe(() => {
      this.clients.update((current) => current.filter((c) => c.id !== client.id));
    });
  }

  private loadClients(): void {
    this.clientService.getAll().subscribe((clients) => this.clients.set(clients));
  }
}
