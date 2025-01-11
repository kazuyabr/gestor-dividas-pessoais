import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { DividasService } from '../../services/dividas.service';
import { Divida } from '../../interfaces/divida.interface';

@Component({
  selector: 'app-lista-dividas',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './lista-dividas.component.html',
  styleUrls: ['./lista-dividas.component.scss']
})
export class ListaDividasComponent implements OnInit {
  dividas: Divida[] = [];
  isLoading = true;
  filtros = {
    status: 'TODOS'
  };

  constructor(
    private dividasService: DividasService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadDividas();
  }

  loadDividas(): void {
    this.dividasService.getDividas().subscribe({
      next: (data) => {
        this.dividas = data;
        this.isLoading = false;
      },
      error: (error) => {
        console.error('Erro ao carregar dívidas:', error);
        this.isLoading = false;
      }
    });
  }

  novaDivida(): void {
    this.router.navigate(['/dividas/criar']);
  }

  editarDivida(id: number): void {
    this.router.navigate([`/dividas/${id}/editar`]);
  }

  excluirDivida(id: number): void {
    if (confirm('Tem certeza que deseja excluir esta dívida?')) {
      this.dividasService.deleteDivida(id).subscribe({
        next: () => {
          this.loadDividas();
        },
        error: (error) => {
          console.error('Erro ao excluir dívida:', error);
        }
      });
    }
  }
}
