import { Component, EventEmitter, Output } from '@angular/core';
import { FiltrosDivida } from '../../interfaces/divida.interface';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-filtros-dividas',
  templateUrl: './filtros-dividas.component.html',
  standalone: true,
  imports: [CommonModule, FormsModule]
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
