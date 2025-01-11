import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { RouterModule, Router } from '@angular/router';
import { LoadingComponent } from '../../../../shared/components/loading/loading.component';
import { trigger, state, style, animate, transition } from '@angular/animations';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterModule, LoadingComponent],
  animations: [
    trigger('notificationAnimation', [
      transition(':enter', [
        style({ transform: 'scaleY(0)', transformOrigin: 'top' }),
        animate('1s ease-out', style({ transform: 'scaleY(1)' }))
      ]),
      transition(':leave', [
        style({ transform: 'scaleY(1)', transformOrigin: 'top' }),
        animate('1s ease-in', style({ transform: 'scaleY(0)' }))
      ])
    ])
  ]
})
export class LoginComponent {
  loginForm: FormGroup;
  isLoading = false;
  errorMessage: string | null = null;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      username: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.loginForm.valid) {
      this.isLoading = true;
      this.errorMessage = null;

      this.authService.login(this.loginForm.value).subscribe({
        next: () => {
          this.router.navigate(['/dashboard']);
        },
        error: (error) => {
          this.isLoading = false;
          switch (error.status) {
            case 401:
              this.errorMessage = 'Senha incorreta';
              break;
            case 404:
              this.errorMessage = 'Email não cadastrado';
              break;
            default:
              this.errorMessage = 'Erro ao realizar login';
          }

          setTimeout(() => {
            this.errorMessage = null;
          }, 5000);
        }
      });
    }
  }
}
