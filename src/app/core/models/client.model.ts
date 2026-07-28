export interface Client {
  id: string;
  name: string;
  phone: string | null;
  addressCount: number;
}

export interface CreateClientRequest {
  name: string;
  phone?: string;
}
