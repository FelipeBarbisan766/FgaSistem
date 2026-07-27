import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '../../../environments/environment';
import {
  CleaningService,
  CleaningServiceSummary,
  CreateCleaningServiceRequest,
} from '../models/cleaning-service.model';

@Injectable({ providedIn: 'root' })
export class CleaningServiceService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = environment.apiUrl;

  getByAddress(addressId: string): Observable<CleaningService[]> {
    return this.http.get<CleaningService[]>(`${this.baseUrl}/addresses/${addressId}/services`);
  }

  create(addressId: string, request: CreateCleaningServiceRequest): Observable<CleaningService> {
    return this.http.post<CleaningService>(`${this.baseUrl}/addresses/${addressId}/services`, request);
  }

  delete(serviceId: string): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/services/${serviceId}`);
  }

  /**
   * Feed global usado pelo Histórico e pelas Alertas (decisão: histórico global,
   * não escopado por serviço/endereço). Cada item já vem com nome do cliente
   * e apelido do endereço, evitando join client-side de 3 coleções.
   */
  getHistory(): Observable<CleaningServiceSummary[]> {
    return this.http.get<CleaningServiceSummary[]>(`${this.baseUrl}/services`);
  }
}
