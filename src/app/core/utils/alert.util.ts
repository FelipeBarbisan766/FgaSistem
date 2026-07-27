import { AlertLevel } from '../models/cleaning-service.model';

const SOON_THRESHOLD_DAYS = 30;

/** Dias entre hoje e a data informada (negativo = já venceu). */
export function daysUntil(dateIso: string): number {
  const dueDate = new Date(dateIso);
  const today = new Date();
  dueDate.setHours(0, 0, 0, 0);
  today.setHours(0, 0, 0, 0);
  return Math.round((dueDate.getTime() - today.getTime()) / 86_400_000);
}

export function getAlertLevel(dateIso: string, soonThresholdDays = SOON_THRESHOLD_DAYS): AlertLevel {
  const remainingDays = daysUntil(dateIso);
  if (remainingDays < 0) return 'overdue';
  if (remainingDays <= soonThresholdDays) return 'soon';
  return 'ok';
}
