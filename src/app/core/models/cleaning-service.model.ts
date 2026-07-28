export type AlertLevel = 'overdue' | 'soon' | 'ok';

export interface CleaningService {
  id: string;
  addressId: string;
  type: string;
  performedAt: string; 
  intervalDays: number;
  nextCleaningDate: string; 
}

export interface CreateCleaningServiceRequest {
  type: string;
  performedAt: string;
  intervalDays: number;
}

export interface CleaningServiceSummary extends CleaningService {
  addressLabel: string;
  clientId: string;
  clientName: string;
}
