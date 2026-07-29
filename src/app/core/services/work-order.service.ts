import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '../../../environments/environment';
import { CreateWorkOrderRequest, UpdateWorkOrderRequest, WorkOrder } from '../models/work-order.model';

@Injectable({ providedIn: 'root' })
export class WorkOrderService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = `${environment.apiUrl}/WorkOrder`;

  getByAddress(addressId: string): Observable<WorkOrder[]> {
    return this.http.get<WorkOrder[]>(`${this.baseUrl}/address/${addressId}`);
  }

  getById(id: string): Observable<WorkOrder> {
    return this.http.get<WorkOrder>(`${this.baseUrl}/${id}`);
  }

  create(addressId: string, request: CreateWorkOrderRequest): Observable<WorkOrder> {
    return this.http.post<WorkOrder>(`${this.baseUrl}/address/${addressId}`, request);
  }

  update(id: string, request: UpdateWorkOrderRequest): Observable<WorkOrder> {
    return this.http.put<WorkOrder>(`${this.baseUrl}/${id}`, request);
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${id}`);
  }

  /**
   * Feed global usado pelo Histórico — GetAll com filtro por query string
   * (ex: ?addressId=, ?clientId=), conforme decisão de rotas flat.
   */
  getAll(params?: { addressId?: string; clientId?: string }): Observable<WorkOrder[]> {
    let query = '';
    if (params?.addressId) query += `?addressId=${params.addressId}`;
    if (params?.clientId) query += `${query ? '&' : '?'}clientId=${params.clientId}`;
    return this.http.get<WorkOrder[]>(`${this.baseUrl}${query}`);
  }

  /**
   * Última WorkOrder de cada endereço — usado no Dashboard de alertas.
   */
  getLatestPerAddress(): Observable<WorkOrder[]> {
    return this.http.get<WorkOrder[]>(`${this.baseUrl}/latests`);
  }
}