import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { DashboardLayoutComponent } from './dashboard-layout.component';
import { DASHBOARD_ROUTES } from './dashboard-layout.routes';

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(DASHBOARD_ROUTES),
    DashboardLayoutComponent
  ]
})
export class DashboardLayoutModule { }
