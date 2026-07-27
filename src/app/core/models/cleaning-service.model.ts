export type AlertLevel = 'overdue' | 'soon' | 'ok';

export interface CleaningService {
  id: string;
  addressId: string;
  type: string;
  performedAt: string; // ISO date
  intervalDays: number;
  /** Pré-calculado pela API (performedAt + intervalDays), consumido direto pelo front. */
  nextCleaningDate: string; // ISO date
}

export interface CreateCleaningServiceRequest {
  type: string;
  performedAt: string;
  intervalDays: number;
}

/**
 * Versão "achatada" de CleaningService usada nas telas que cruzam
 * Client -> Address -> Service (Dashboard, Histórico global, Alertas),
 * evitando que o Angular precise fazer join de 3 coleções em memória.
 */
export interface CleaningServiceSummary extends CleaningService {
  addressLabel: string;
  clientId: string;
  clientName: string;
}
