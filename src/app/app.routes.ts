import { Routes } from '@angular/router';
import { ShellComponent } from './layout/shell/shell.component';

export const routes: Routes = [
  {
    path: '',
    component: ShellComponent,
    children: [
      {
        path: '',
        loadComponent: () =>
          import('./features/dashboard/dashboard.component').then((m) => m.DashboardComponent),
        title: 'Painel — FgaSistem',
      },
      {
        path: 'clientes',
        loadComponent: () =>
          import('./features/clients/client-list/client-list.component').then(
            (m) => m.ClientListComponent,
          ),
        title: 'Clientes — FgaSistem',
      },
      {
        path: 'clientes/:id',
        loadComponent: () =>
          import('./features/clients/client-detail/client-detail.component').then(
            (m) => m.ClientDetailComponent,
          ),
        title: 'Cliente — FgaSistem',
      },
      {
        path: 'servicos',
        loadComponent: () =>
          import('./features/services-history/services-history.component').then(
            (m) => m.ServicesHistoryComponent,
          ),
        title: 'Histórico — FgaSistem',
      },
      {
        path: 'alertas',
        loadComponent: () =>
          import('./features/alerts/alerts.component').then((m) => m.AlertsComponent),
        title: 'Alertas — FgaSistem',
      },
      { path: '**', redirectTo: '' },
    ],
  },
];
