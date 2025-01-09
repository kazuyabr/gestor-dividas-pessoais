import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CommonModule } from '@angular/common';
import { DashboardComponent } from '../../components/dashboard/dashboard.component';
import { DashboardService } from '../../services/dashboard.service';
import { of } from 'rxjs';

describe('DashboardComponent', () => {
  let component: DashboardComponent;
  let fixture: ComponentFixture<DashboardComponent>;

  beforeEach(async () => {
    const dashboardService = {
      getDashboardSummary: () => of({
        totalDividas: 0,
        dividasVencidas: 0,
        dividasPagas: 0,
        totalValorPendente: 0
      })
    };

    await TestBed.configureTestingModule({
      imports: [DashboardComponent, HttpClientTestingModule, CommonModule],
      providers: [{ provide: DashboardService, useValue: dashboardService }]
    }).compileComponents();

    fixture = TestBed.createComponent(DashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
