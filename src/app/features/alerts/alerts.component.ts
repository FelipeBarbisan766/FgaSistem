import { ChangeDetectionStrategy, Component, computed, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';

import { CleaningServiceService } from '../../core/services/cleaning-service.service';
import { CleaningServiceSummary } from '../../core/models/cleaning-service.model';
import { daysUntil, getAlertLevel } from '../../core/utils/alert.util';
import { formatDate } from '../../core/utils/date.util';

@Component({
  selector: 'app-alerts',
  imports: [RouterLink],
  templateUrl: './alerts.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AlertsComponent {
  private readonly cleaningServiceService = inject(CleaningServiceService);

  protected readonly services = signal<CleaningServiceSummary[]>([]);

  protected readonly overdue = computed(() =>
    this.services()
      .filter((service) => getAlertLevel(service.nextCleaningDate) === 'overdue')
      .sort((a, b) => daysUntil(a.nextCleaningDate) - daysUntil(b.nextCleaningDate)),
  );

  protected readonly soon = computed(() =>
    this.services()
      .filter((service) => getAlertLevel(service.nextCleaningDate) === 'soon')
      .sort((a, b) => daysUntil(a.nextCleaningDate) - daysUntil(b.nextCleaningDate)),
  );

  protected readonly formatDate = formatDate;
  protected readonly daysUntilOf = daysUntil;

  constructor() {
    this.cleaningServiceService.getHistory().subscribe((services) => this.services.set(services));
  }
}
