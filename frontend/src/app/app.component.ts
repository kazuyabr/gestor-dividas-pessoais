import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, RouterOutlet } from '@angular/router';
import { LoadingComponent } from './core/components/loading/loading.component';

@Component({
  selector: 'app-root',
  template: `
    <app-loading *ngIf="isLoading"></app-loading>
    <router-outlet *ngIf="!isLoading"></router-outlet>
  `,
  standalone: true,
  imports: [CommonModule, RouterModule, RouterOutlet, LoadingComponent]
})
export class AppComponent implements OnInit {
  isLoading = true;

  ngOnInit() {
    setTimeout(() => {
      this.isLoading = false;
    }, 800);
  }
}
