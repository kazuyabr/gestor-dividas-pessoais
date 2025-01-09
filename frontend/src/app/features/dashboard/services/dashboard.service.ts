import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { DashboardSummary, DividaResumo } from '../interfaces/dashboard.interface';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {
  constructor(private http: HttpClient) {}

  getDashboardSummary(): Observable<DashboardSummary> {
    return this.http.get<DividaResumo[]>('/dividas/').pipe(
      map(dividas => this.calcularResumo(dividas))
    );
  }

  private calcularResumo(dividas: DividaResumo[]): DashboardSummary {
    const hoje = new Date();
    return {
      totalDividas: dividas.length,
      totalValorPendente: dividas
        .filter(d => d.status === 'Pendente')
        .reduce((acc, curr) => acc + curr.valor, 0),
      dividasPagas: dividas.filter(d => d.status === 'Pago').length,
      dividasVencidas: dividas.filter(d => {
        return new Date(d.dataVencimento) < hoje && d.status === 'Pendente'
      }).length
    };
  }
}
