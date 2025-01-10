import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Divida, DividaBase } from '../interfaces/divida.interface';

@Injectable({
  providedIn: 'root'
})
export class DividasService {
  constructor(private http: HttpClient) {}

  listarDividas(): Observable<Divida[]> {
    return this.http.get<Divida[]>('/dividas/');
  }

  obterDivida(id: number): Observable<Divida> {
    return this.http.get<Divida>(`/dividas/${id}`);
  }

  criarDivida(divida: DividaBase, usuario_id: number): Observable<Divida> {
    return this.http.post<Divida>(`/dividas/?usuario_id=${usuario_id}`, divida);
  }

  atualizarDivida(id: number, divida: Partial<Divida>): Observable<Divida> {
    return this.http.put<Divida>(`/dividas/${id}`, divida);
  }

  excluirDivida(id: number): Observable<void> {
    return this.http.delete<void>(`/dividas/${id}`);
  }
}
