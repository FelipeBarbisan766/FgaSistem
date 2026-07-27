import { CleaningServiceSummary } from './cleaning-service.model';

export interface DashboardSummary {
  totalClients: number;
  totalAddresses: number;
  overdueServices: CleaningServiceSummary[];
  soonServices: CleaningServiceSummary[];
  recentServices: CleaningServiceSummary[];
}
