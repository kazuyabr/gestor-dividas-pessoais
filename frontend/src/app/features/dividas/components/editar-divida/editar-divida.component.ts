import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { DividasService } from '../../services/dividas.service';

@Component({
  selector: 'app-editar-divida',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './editar-divida.component.html',
  styleUrls: ['./editar-divida.component.scss']
})
export class EditarDividaComponent implements OnInit {
  dividaForm: FormGroup;
  isLoading = false;
  dividaId: number;

  constructor(
    private fb: FormBuilder,
    private dividasService: DividasService,
    private router: Router,
    private route: ActivatedRoute
  ) {
    this.dividaForm = this.fb.group({
      titulo: ['', Validators.required],
      valor: ['', [Validators.required, Validators.min(0)]],
      data_vencimento: ['', Validators.required],
      status: ['', Validators.required],
      observacoes: ['']
    });

    this.dividaId = Number(this.route.snapshot.paramMap.get('id'));
  }

  ngOnInit(): void {
    this.loadDivida();
  }

  loadDivida(): void {
    this.isLoading = true;
    this.dividasService.getDividaById(this.dividaId).subscribe({
      next: (divida) => {
        const dataVencimento = new Date(divida.data_vencimento)
          .toISOString()
          .substring(0, 10);

        this.dividaForm.patchValue({
          ...divida,
          data_vencimento: dataVencimento
        });
        this.isLoading = false;
      },
      error: (error) => {
        console.error('Erro ao carregar dívida:', error);
        this.isLoading = false;
      }
    });
  }

  onSubmit(): void {
    if (this.dividaForm.valid) {
      this.isLoading = true;
      this.dividasService.updateDivida(this.dividaId, this.dividaForm.value).subscribe({
        next: () => {
          this.router.navigate(['/dividas']);
        },
        error: (error) => {
          console.error('Erro ao atualizar dívida:', error);
          this.isLoading = false;
        }
      });
    }
  }
}
