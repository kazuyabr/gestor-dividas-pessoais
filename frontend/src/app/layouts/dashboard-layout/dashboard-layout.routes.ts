import { Routes } from '@angular/router';
import { DashboardLayoutComponent } from './dashboard-layout.component';

export const DASHBOARD_ROUTES: Routes = [
  {
    path: '',
    component: DashboardLayoutComponent,
    children: [
      {
        path: 'dashboard',
        loadChildren: () => import('../../features/dashboard/dashboard.module')
          .then(m => m.DashboardModule)
      },
      {
        path: 'dividas',
        loadChildren: () => import('../../features/dividas/dividas.module')
          .then(m => m.DividasModule)
      }
    ]
  }
];
