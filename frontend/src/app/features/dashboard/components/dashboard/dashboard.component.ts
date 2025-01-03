import { Component, OnInit } from '@angular/core';
import { DashboardService } from '../../services/dashboard.service';
import { DashboardSummary } from '../../interfaces/dashboard.interface';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  imports: [CommonModule],
  standalone: true
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
