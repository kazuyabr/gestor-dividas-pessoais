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

  ngOnInit() {
    // Força o tema escuro na home
    document.body.classList.add('dark-theme')

    setTimeout(() => {
      this.isLoading = false
    }, 800)
  }

  // Ao destruir o componente, restauramos o tema original do usuário
  ngOnDestroy() {
    const userTheme = localStorage.getItem('theme')
    if (userTheme !== 'dark') {
      document.body.classList.remove('dark-theme')
    }
  }
}
