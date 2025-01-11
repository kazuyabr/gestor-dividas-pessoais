import { Component, OnInit } from '@angular/core';
import { DashboardService } from '../../services/dashboard.service';
import { DashboardSummary } from '../../interfaces/dashboard.interface';
import { NavMenuComponent } from '../../../../shared/components/nav-menu/nav-menu.component';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { LoadingComponent } from '../../../../shared/components/loading/loading.component';
import { trigger, transition, style, animate } from '@angular/animations';
  @Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.scss'],
    imports: [CommonModule, RouterModule, LoadingComponent],
    standalone: true,
    animations: [
      trigger('fadeIn', [
        transition(':enter', [
          style({ opacity: 0, transform: 'translateY(10px)' }),
          animate('300ms ease-out', style({ opacity: 1, transform: 'translateY(0)' }))
        ])
      ])
    ]
})export class DashboardComponent implements OnInit {
  summary: DashboardSummary | null = null;
  isLoading = true;
  error: string | null = null;

  constructor(private dashboardService: DashboardService) {}

  ngOnInit(): void {
    this.loadDashboardData();
  }

  private loadDashboardData(): void {
    this.dashboardService.getDashboardSummary().subscribe({
      next: (data) => {
        this.summary = data;
        this.isLoading = false;
      },
      error: (error) => {
        this.error = 'Erro ao carregar dados do dashboard';
        this.isLoading = false;
        console.error('Erro:', error);
      }
    });
  }
}
