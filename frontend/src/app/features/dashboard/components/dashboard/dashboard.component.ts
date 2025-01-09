import { Component, OnInit } from '@angular/core';
import { DashboardService } from '../../services/dashboard.service';
import { DashboardSummary } from '../../interfaces/dashboard.interface';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  template: `
    <div class="dashboard">
      <h1>Dashboard</h1>
      <div class="summary" *ngIf="summary">
        <div class="card">
          <h3>Total de Dívidas</h3>
          <p>{{summary.totalDividas}}</p>
        </div>
        <div class="card">
          <h3>Valor Pendente</h3>
          <p>R$ {{summary.totalValorPendente | number:'1.2-2'}}</p>
        </div>
        <div class="card">
          <h3>Dívidas Pagas</h3>
          <p>{{summary.dividasPagas}}</p>
        </div>
        <div class="card">
          <h3>Dívidas Vencidas</h3>
          <p>{{summary.dividasVencidas}}</p>
        </div>
      </div>
      <div class="actions">
        <button routerLink="/dividas">Gerenciar Dívidas</button>
      </div>
    </div>
  `,
  styles: [`
    .dashboard {
      padding: 20px
    }
    .summary {
      display: grid
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))
      gap: 20px
      margin: 20px 0
    }
    .card {
      padding: 20px
      border-radius: 8px
      background: #fff
      box-shadow: 0 2px 4px rgba(0,0,0,0.1)
    }
  `],
  standalone: true,
  imports: [CommonModule, RouterModule]
})
export class DashboardComponent implements OnInit {
  summary: DashboardSummary | null = null;

  constructor(private dashboardService: DashboardService) {}

  ngOnInit(): void {
    this.loadDashboardData();
  }

  private loadDashboardData(): void {
    this.dashboardService.getDashboardSummary().subscribe({
      next: (data) => this.summary = data,
      error: (error) => console.error('Erro ao carregar dashboard:', error)
    });
  }
}
