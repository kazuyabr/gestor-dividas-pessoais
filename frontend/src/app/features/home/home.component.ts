import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  standalone: true,
  imports: [CommonModule, RouterModule]
})
export class HomeComponent implements OnInit {
  isLoading = true
  isDarkMode = localStorage.getItem('theme') === 'dark'

  ngOnInit() {
    if (this.isDarkMode) {
      document.body.classList.add('dark-theme')
    }
    setTimeout(() => {
      this.isLoading = false
    }, 800)
  }

  toggleTheme() {
    this.isDarkMode = !this.isDarkMode
    document.body.classList.toggle('dark-theme')
    localStorage.setItem('theme', this.isDarkMode ? 'dark' : 'light')
  }
}
