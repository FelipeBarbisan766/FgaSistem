export const WORK_ORDER_TYPES = ['CleaningJob', 'PruningJob', 'InstallationJob', 'Outers'] as const;
export type WorkOrderType = (typeof WORK_ORDER_TYPES)[number];

export const WORK_ORDER_TYPE_LABELS: Record<WorkOrderType, string> = {
  CleaningJob: 'Limpeza de painel solar',
  PruningJob: 'Poda',
  InstallationJob: 'Instalação',
  Outers: 'Outros',
};

export interface WorkOrder {
  id: string;
  isActive: boolean;
  type: WorkOrderType;
  price: number | null;
  quantity: number | null;
  date: string;
  description: string | null;
  daysSinceCompleted: number;
  addressId: string;
  clientId: string;
  clientName: string;
}

export interface CreateWorkOrderRequest {
  type: WorkOrderType;
  price: number | null;
  quantity: number | null;
  date: string;
  description: string | null;
}

export interface UpdateWorkOrderRequest extends CreateWorkOrderRequest {}