import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DividasService } from '../../services/dividas.service';

@Component({
  selector: 'app-criar-divida',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './criar-divida.component.html',
  styleUrls: ['./criar-divida.component.scss']
})
export class CriarDividaComponent {
  dividaForm: FormGroup;
  isLoading = false;

  constructor(
    private fb: FormBuilder,
    private dividasService: DividasService,
    private router: Router
  ) {
    this.dividaForm = this.fb.group({
      titulo: ['', Validators.required],
      valor: ['', [Validators.required, Validators.min(0)]],
      data_vencimento: ['', Validators.required],
      status: ['PENDENTE', Validators.required],
      observacoes: ['']
    });
  }

  onSubmit(): void {
    if (this.dividaForm.valid) {
      this.isLoading = true;
      this.dividasService.createDivida(this.dividaForm.value).subscribe({
        next: () => {
          this.router.navigate(['/dividas']);
        },
        error: (error) => {
          console.error('Erro ao criar dívida:', error);
          this.isLoading = false;
        }
      });
    }
  }
}
