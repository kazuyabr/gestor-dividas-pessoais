import { Component, EventEmitter, Output } from '@angular/core';
import { FiltrosDivida } from '../../interfaces/divida.interface';

@Component({
  selector: 'app-filtros-dividas',
  templateUrl: './filtros-dividas.component.html',
  styleUrls: ['./filtros-dividas.component.scss']
})
export class FiltrosDividasComponent {
  @Output() filtrosChange = new EventEmitter<FiltrosDivida>();

  filtros: FiltrosDivida = {
    status: '',
    ordenacao: 'asc',
    campo: 'dataVencimento'
  };

  aplicarFiltros(): void {
    this.filtrosChange.emit(this.filtros);
  }
}
