import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { DividasService } from '../../services/dividas.service';
import { Divida } from '../../interfaces/divida.interface';

@Component({
  selector: 'app-form-divida',
  templateUrl: './form-divida.component.html',
  styleUrls: ['./form-divida.component.scss']
})
export class FormDividaComponent implements OnInit {
  dividaForm: FormGroup;
  isEdicao = false;
  dividaId?: number;

  constructor(
    private fb: FormBuilder,
    private dividasService: DividasService,
    private router: Router,
    private route: ActivatedRoute
  ) {
    this.dividaForm = this.fb.group({
      titulo: ['', Validators.required],
      valor: ['', [Validators.required, Validators.min(0)]],
      dataVencimento: ['', Validators.required],
      status: ['Pendente', Validators.required],
      observacoes: ['']
    });
  }

  ngOnInit(): void {
    this.dividaId = Number(this.route.snapshot.paramMap.get('id'));
    if (this.dividaId) {
      this.isEdicao = true;
      this.carregarDivida(this.dividaId);
    }
  }

  carregarDivida(id: number): void {
    this.dividasService.obterDivida(id).subscribe({
      next: (divida) => this.dividaForm.patchValue(divida),
      error: (error) => console.error('Erro ao carregar dívida:', error)
    });
  }

  onSubmit(): void {
    if (this.dividaForm.valid) {
      const divida = this.dividaForm.value;

      if (this.isEdicao && this.dividaId) {
        this.dividasService.atualizarDivida(this.dividaId, divida).subscribe({
          next: () => this.router.navigate(['/dividas']),
          error: (error) => console.error('Erro ao atualizar dívida:', error)
        });
      } else {
        this.dividasService.criarDivida(divida, 1).subscribe({
          next: () => this.router.navigate(['/dividas']),
          error: (error) => console.error('Erro ao criar dívida:', error)
        });
      }
    }
  }
}
