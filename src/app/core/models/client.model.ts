export interface Client {
  id: string;
  name: string;
  email: string | null;
  phone: string | null;
  /** Projeção calculada pela API (COUNT via join), não persistida. */
  addressCount: number;
}

export interface CreateClientRequest {
  name: string;
  email?: string;
  phone?: string;
}
