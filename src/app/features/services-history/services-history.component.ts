import { ChangeDetectionStrategy, Component, computed, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';

import { CleaningServiceService } from '../../core/services/cleaning-service.service';
import { ClientService } from '../../core/services/client.service';
import { CleaningServiceSummary } from '../../core/models/cleaning-service.model';
import { Client } from '../../core/models/client.model';
import { formatDate } from '../../core/utils/date.util';

@Component({
  selector: 'app-services-history',
  imports: [RouterLink],
  templateUrl: './services-history.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ServicesHistoryComponent {
  private readonly cleaningServiceService = inject(CleaningServiceService);
  private readonly clientService = inject(ClientService);

  protected readonly services = signal<CleaningServiceSummary[]>([]);
  protected readonly clients = signal<Client[]>([]);
  protected readonly searchTerm = signal('');
  protected readonly clientFilter = signal('');

  protected readonly filteredServices = computed(() => {
    const term = this.searchTerm().trim().toLowerCase();
    const clientId = this.clientFilter();

    return this.services()
      .filter((service) => !clientId || service.clientId === clientId)
      .filter((service) => {
        if (!term) return true;
        return (
          service.type.toLowerCase().includes(term) ||
          service.addressLabel.toLowerCase().includes(term) ||
          service.clientName.toLowerCase().includes(term)
        );
      })
      .sort((a, b) => +new Date(b.performedAt) - +new Date(a.performedAt));
  });

  protected readonly formatDate = formatDate;

  constructor() {
    this.cleaningServiceService.getHistory().subscribe((services) => this.services.set(services));
    this.clientService.getAll().subscribe((clients) => this.clients.set(clients));
  }

  protected updateSearchTerm(value: string): void {
    this.searchTerm.set(value);
  }

  protected updateClientFilter(value: string): void {
    this.clientFilter.set(value);
  }
}
