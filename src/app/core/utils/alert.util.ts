export type AlertLevel = 'overdue' | 'soon' | 'ok';

// TODO: hoje fixo em 180 dias (6 meses). Se um dia precisar variar por serviço, isso vira parâmetro.
const CLEANING_INTERVAL_DAYS = 180;
const SOON_THRESHOLD_DAYS = 30;

export function daysUntilNext(daysSinceCompleted: number): number {
  return CLEANING_INTERVAL_DAYS - daysSinceCompleted;
}

export function getAlertLevel(daysSinceCompleted: number): AlertLevel {
  const remaining = daysUntilNext(daysSinceCompleted);
  if (remaining < 0) return 'overdue';
  if (remaining <= SOON_THRESHOLD_DAYS) return 'soon';
  return 'ok';
}