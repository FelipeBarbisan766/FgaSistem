import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '../../../environments/environment';
import { Client, CreateClientRequest } from '../models/client.model';

@Injectable({ providedIn: 'root' })
export class ClientService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = `${environment.apiUrl}/client`;

  getAll(): Observable<Client[]> {
    return this.http.get<Client[]>(this.baseUrl);
  }

  getById(clientId: string): Observable<Client> {
    return this.http.get<Client>(`${this.baseUrl}/${clientId}`);
  }

  create(request: CreateClientRequest): Observable<Client> {
    return this.http.post<Client>(this.baseUrl, request);
  }

  delete(clientId: string): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${clientId}`);
  }
}
