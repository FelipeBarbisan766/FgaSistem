// import { ChangeDetectionStrategy, Component, computed, inject, signal } from '@angular/core';
// import { RouterLink } from '@angular/router';

// import { DashboardService } from '../../core/services/dashboard.service';
// import { DashboardSummary } from '../../core/models/dashboard-summary.model';
// import { daysUntil, getAlertLevel } from '../../core/utils/alert.util';
// import { formatDate } from '../../core/utils/date.util';

// @Component({
//   selector: 'app-dashboard',
//   imports: [RouterLink],
//   templateUrl: './dashboard.component.html',
//   changeDetection: ChangeDetectionStrategy.OnPush,
// })
// export class DashboardComponent {
//   private readonly dashboardService = inject(DashboardService);

//   protected readonly summary = signal<DashboardSummary | null>(null);

//   protected readonly overdueCount = computed(() => this.summary()?.overdueServices.length ?? 0);
//   protected readonly soonCount = computed(() => this.summary()?.soonServices.length ?? 0);

//   protected readonly upcoming = computed(() =>
//     [...(this.summary()?.overdueServices ?? []), ...(this.summary()?.soonServices ?? [])]
//       .sort((a, b) => daysUntil(a.nextCleaningDate) - daysUntil(b.nextCleaningDate))
//       .slice(0, 6),
//   );

//   protected readonly recent = computed(() => this.summary()?.recentServices.slice(0, 5) ?? []);

//   protected readonly formatDate = formatDate;
//   protected readonly alertLevelOf = getAlertLevel;
//   protected readonly daysUntilOf = daysUntil;

//   constructor() {
//     this.dashboardService.getSummary().subscribe((summary) => this.summary.set(summary));
//   }
// }
