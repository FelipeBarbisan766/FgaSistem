export interface Client {
  id: string;
  name: string;
  phoneNumber: string | null;
  addressCount: number;
  alias?: string;
}

export interface CreateClientRequest {
  name: string;
  phoneNumber?: string;
  alias?: string;
}
