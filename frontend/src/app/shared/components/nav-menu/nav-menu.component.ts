import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../../features/auth/services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav-menu',
  templateUrl: './nav-menu.component.html',
  styleUrls: ['./nav-menu.component.scss'],
  standalone: true,
  imports: [CommonModule, RouterModule]
})
export class NavMenuComponent implements OnInit {
  isDarkMode = localStorage.getItem('theme') === 'dark';
  menuItems = [
    { path: '/dashboard', label: 'Dashboard', icon: 'chart-line' },
    { path: '/dividas', label: 'Dívidas', icon: 'money-bill-wave' }
  ];

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit() {
    if (this.isDarkMode) {
      document.body.classList.add('dark-theme');
    }
  }

  logout() {
    this.authService.logout();
    this.router.navigate(['/auth/login']);
  }

  toggleTheme() {
    this.isDarkMode = !this.isDarkMode;
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', this.isDarkMode ? 'dark' : 'light');
  }
}
