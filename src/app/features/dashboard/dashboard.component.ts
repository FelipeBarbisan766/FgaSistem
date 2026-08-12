import { ChangeDetectionStrategy, Component, computed, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';

import { DashboardService } from '../../core/services/dashboard.service';
import { DashboardSummary } from '../../core/models/dashboard-summary.model';
import { getAlertLevel } from '../../core/utils/alert.util';
import { formatDate } from '../../core/utils/date.util';

@Component({
  selector: 'app-dashboard',
  imports: [RouterLink],
  templateUrl: './dashboard.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DashboardComponent {
  private readonly dashboardService = inject(DashboardService);

  protected readonly summary = signal<DashboardSummary | null>(null);

  protected readonly totalClients = computed(() => this.summary()?.totalClients ?? 0);
  protected readonly totalAddresses = computed(() => this.summary()?.totalAddresses ?? 0);

  private readonly alertedWorkOrders = computed(() =>
    (this.summary()?.latestPerAddress ?? []).filter(
      (workOrder) => getAlertLevel(workOrder.daysSinceCompleted) !== 'ok',
    ),
  );

  protected readonly overdueCount = computed(
    () => this.alertedWorkOrders().filter((w) => getAlertLevel(w.daysSinceCompleted) === 'overdue').length,
  );
  protected readonly soonCount = computed(
    () => this.alertedWorkOrders().filter((w) => getAlertLevel(w.daysSinceCompleted) === 'soon').length,
  );

  protected readonly upcoming = computed(() =>
    [...this.alertedWorkOrders()].sort((a, b) => b.daysSinceCompleted - a.daysSinceCompleted).slice(0, 6),
  );

  protected readonly recent = computed(() => this.summary()?.recentWorkOrders.slice(0, 5) ?? []);

  protected readonly formatDate = formatDate;
  protected readonly alertLevelOf = getAlertLevel;

  constructor() {
    this.dashboardService.getSummary().subscribe((summary) => this.summary.set(summary));
  }
}