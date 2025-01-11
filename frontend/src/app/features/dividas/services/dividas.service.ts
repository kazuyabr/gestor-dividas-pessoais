import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../../environments/environment';
import { Divida, DividaCreate, DividaUpdate } from '../interfaces/divida.interface';

@Injectable({
  providedIn: 'root'
})
export class DividasService {
  private baseUrl = `${environment.apiUrl}:${environment.apiPort}/api/${environment.apiVersion}/dividas`;

  constructor(private http: HttpClient) {}

  getDividas(): Observable<Divida[]> {
    return this.http.get<Divida[]>(this.baseUrl);
  }

  getDividaById(id: number): Observable<Divida> {
    return this.http.get<Divida>(`${this.baseUrl}/${id}`);
  }

  createDivida(divida: DividaCreate): Observable<Divida> {
    return this.http.post<Divida>(this.baseUrl, divida);
  }

  updateDivida(id: number, divida: DividaUpdate): Observable<Divida> {
    return this.http.put<Divida>(`${this.baseUrl}/${id}`, divida);
  }

  deleteDivida(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${id}`);
  }
}
