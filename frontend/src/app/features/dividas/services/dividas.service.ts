import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Divida, DividaCreate, FiltrosDivida } from '../interfaces/divida.interface';

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

  criarDivida(divida: DividaCreate, usuario_id: number): Observable<Divida> {
    return this.http.post<Divida>(`/dividas/?usuario_id=${usuario_id}`, divida);
  }

  atualizarDivida(id: number, divida: Partial<Divida>): Observable<Divida> {
    return this.http.put<Divida>(`/dividas/${id}`, divida);
  }

  excluirDivida(id: number): Observable<void> {
    return this.http.delete<void>(`/dividas/${id}`);
  }
}

  confirmarEExcluirDivida(id: number): Observable<boolean> {
    return new Observable(observer => {
      const confirmacao = confirm('Tem certeza que deseja excluir esta dívida?');

      if (confirmacao) {
        this.excluirDivida(id).subscribe({
          next: () => {
            observer.next(true);
            observer.complete();
          },
          error: (error) => {
            observer.error(error);
            observer.complete();
          }
        });
      } else {
        observer.next(false);
        observer.complete();
      }
    });
  }
