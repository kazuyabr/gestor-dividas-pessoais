import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Router } from '@angular/router';
import { AuthService } from '../../../features/auth/services/auth.service';

@Component({
  selector: 'app-nav-menu',
  templateUrl: './nav-menu.component.html',
  styleUrls: ['./nav-menu.component.scss'],
  standalone: true,
  imports: [CommonModule, RouterModule]
})
export class NavMenuComponent {
  isDarkMode = localStorage.getItem('theme') === 'dark';
  menuItems = [
    { path: '/dashboard', label: 'Dashboard', icon: 'chart-line' },
    { path: '/dividas', label: 'Dívidas', icon: 'money-bill-wave' }
  ];

  constructor(
    private authService: AuthService,
    private router: Router
  ) {
    if (this.isDarkMode) {
      document.body.classList.add('dark-theme');
    }
  }

  isActive(path: string): boolean {
    return this.router.isActive(path, {
      paths: 'exact',
      queryParams: 'exact',
      fragment: 'ignored',
      matrixParams: 'ignored'
    });
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/auth/login']);
  }

  toggleTheme(): void {
    this.isDarkMode = !this.isDarkMode;
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', this.isDarkMode ? 'dark' : 'light');
  }
}
