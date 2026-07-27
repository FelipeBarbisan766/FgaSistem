import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '../../../environments/environment';
import { Address, CreateAddressRequest } from '../models/address.model';

@Injectable({ providedIn: 'root' })
export class AddressService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = environment.apiUrl;

  getByClient(clientId: string): Observable<Address[]> {
    return this.http.get<Address[]>(`${this.baseUrl}/clients/${clientId}/addresses`);
  }

  create(clientId: string, request: CreateAddressRequest): Observable<Address> {
    return this.http.post<Address>(`${this.baseUrl}/clients/${clientId}/addresses`, request);
  }

  delete(addressId: string): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/addresses/${addressId}`);
  }
}
