import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DividasService } from '../../services/dividas.service';
import { Divida } from '../../interfaces/divida.interface';

@Component({
  selector: 'app-lista-dividas',
  templateUrl: './lista-dividas.component.html',
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class ListaDividasComponent implements OnInit {
  dividas: Divida[] = [];
  filtros = {
    status: '',
    ordenacao: 'asc',
    campo: 'dataVencimento'
  };

  constructor(private dividasService: DividasService) {}

  ngOnInit(): void {
    this.carregarDividas();
  }

  carregarDividas(): void {
    this.dividasService.listarDividas().subscribe({
      next: (dividas) => this.dividas = dividas,
      error: (error) => console.error('Erro ao carregar dívidas:', error)
    });
  }

  excluirDivida(id: number): void {
    if (confirm('Deseja realmente excluir esta dívida?')) {
      this.dividasService.excluirDivida(id).subscribe({
        next: () => this.carregarDividas(),
        error: (error) => console.error('Erro ao excluir dívida:', error)
      });
    }
  }

  aplicarFiltros(): void {
    let dividasFiltradas = [...this.dividas];

    if (this.filtros.status) {
      dividasFiltradas = dividasFiltradas.filter(d => d.status === this.filtros.status);
    }

    this.dividas = dividasFiltradas.sort((a, b) => {
      const fator = this.filtros.ordenacao === 'asc' ? 1 : -1;
      const valorA = String(a[this.filtros.campo as keyof Divida]);
      const valorB = String(b[this.filtros.campo as keyof Divida]);
      return valorA > valorB ? fator : -fator;
    });
  }
}
