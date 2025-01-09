import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-loading',
  template: `
    <div class="loading-overlay">
      <div class="loading-spinner">
        <div class="spinner"></div>
        <p>Carregando...</p>
      </div>
    </div>
  `,
  styles: [`
    .loading-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: var(--bg-primary);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 9999;
    }

    .loading-spinner {
      text-align: center;
    }

    .spinner {
      width: 50px;
      height: 50px;
      border: 3px solid var(--accent-primary);
      border-radius: 50%;
      border-top-color: transparent;
      animation: spin 1s linear infinite;
      margin: 0 auto 1rem;
    }

    p {
      color: var(--text-primary);
      font-size: 1.1rem;
    }

    @keyframes spin {
      to {
        transform: rotate(360deg);
      }
    }
  `],

  standalone: true,
  imports: [CommonModule]
})
export class LoadingComponent {}
