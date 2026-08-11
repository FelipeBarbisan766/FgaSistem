import { ChangeDetectionStrategy, Component, computed, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';

import { WorkOrderService } from '../../core/services/work-order.service';
import { WorkOrder, WORK_ORDER_TYPE_LABELS } from '../../core/models/work-order.model';
import { formatDate } from '../../core/utils/date.util';

@Component({
  selector: 'app-work-order-history',
  imports: [RouterLink],
  templateUrl: './work-order-history.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class WorkOrderHistoryComponent {
  private readonly workOrderService = inject(WorkOrderService);

  protected readonly workOrders = signal<WorkOrder[]>([]);
  protected readonly searchTerm = signal('');
  protected readonly clientFilter = signal('');

  protected readonly clientOptions = computed(() => {
    const seen = new Map<string, string>();
    for (const workOrder of this.workOrders()) {
      seen.set(workOrder.address.client.id, workOrder.address.client.name);
    }
    return Array.from(seen, ([id, name]) => ({ id, name }));
  });

  protected readonly filteredWorkOrders = computed(() => {
    const term = this.searchTerm().trim().toLowerCase();
    const clientId = this.clientFilter();

    return this.workOrders()
      .filter((workOrder) => !clientId || workOrder.address.client.id === clientId)
      .filter((workOrder) => {
        if (!term) return true;
        return (
          workOrder.type.toLowerCase().includes(term) ||
          workOrder.address.client.name.toLowerCase().includes(term) ||
          (workOrder.description ?? '').toLowerCase().includes(term)
        );
      })
      .sort((a, b) => +new Date(b.date) - +new Date(a.date));
  });

  protected readonly formatDate = formatDate;
  protected readonly typeLabels = WORK_ORDER_TYPE_LABELS;

  constructor() {
    this.workOrderService.getLatestPerAddress().subscribe((workOrders) => this.workOrders.set(workOrders));
  }

  protected updateSearchTerm(value: string): void {
    this.searchTerm.set(value);
  }

  protected updateClientFilter(value: string): void {
    this.clientFilter.set(value);
  }
}