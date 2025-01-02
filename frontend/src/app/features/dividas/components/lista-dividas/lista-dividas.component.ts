import { Component, OnInit } from '@angular/core';
import { DividasService } from '../../services/dividas.service';
import { Divida, FiltrosDivida } from '../../interfaces/divida.interface';

@Component({
  selector: 'app-lista-dividas',
  templateUrl: './lista-dividas.component.html',
  styleUrls: ['./lista-dividas.component.scss']
})
export class ListaDividasComponent implements OnInit {
  dividas: Divida[] = [];
  filtros: FiltrosDivida = {};

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

  handleExclusao(id: number): void {
    this.dividasService.confirmarEExcluirDivida(id).subscribe({
      next: (confirmado) => {
        if (confirmado) {
          this.carregarDividas();
        }
      },
      error: (error) => console.error('Erro ao excluir dívida:', error)
    });
  }
}

  aplicarFiltros(filtros: FiltrosDivida): void {
    this.dividas = this.dividas.sort((a, b) => {
      const fator = filtros.ordenacao === 'asc' ? 1 : -1;

      switch(filtros.campo) {
        case 'titulo':
          return fator * a.titulo.localeCompare(b.titulo);
        case 'valor':
          return fator * (a.valor - b.valor);
        case 'dataVencimento':
          return fator * (new Date(a.dataVencimento).getTime() - new Date(b.dataVencimento).getTime());
        default:
          return 0;
      }
    });

    if (filtros.status) {
      this.dividas = this.dividas.filter(d => d.status === filtros.status);
    }
  }
