export interface Address {
  id: string;
  clientId: string;
  label: string;
  street: string;
  city: string | null;
}

export interface CreateAddressRequest {
  label: string;
  street: string;
  city?: string;
}
