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
   * Última WorkOrder de cada endereço, com Address e Client aninhados —
   * usado no Dashboard de alertas e agora também no Histórico.
   */
  getLatestPerAddress(): Observable<WorkOrder[]> {
    return this.http.get<WorkOrder[]>(`${this.baseUrl}/latests`);
  }
}