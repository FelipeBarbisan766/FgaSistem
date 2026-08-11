import { WorkOrder } from './work-order.model';

export interface DashboardSummary {
  totalClients: number;
  totalAddresses: number;
  latestPerAddress: WorkOrder[];
  recentWorkOrders: WorkOrder[];
}