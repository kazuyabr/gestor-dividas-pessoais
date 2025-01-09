import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CommonModule } from '@angular/common';
import { ListaDividasComponent } from './lista-dividas.component';
import { DividasService } from '../../services/dividas.service';
import { Divida } from '../../interfaces/divida.interface';
import { of } from 'rxjs';

describe('ListaDividasComponent', () => {
  let component: ListaDividasComponent;
  let fixture: ComponentFixture<ListaDividasComponent>;
  let dividasService: jasmine.SpyObj<DividasService>;

  beforeEach(async () => {
    const mockDividas: Divida[] = [{
      id: 1,
      titulo: 'Teste',
      valor: 100,
      status: 'Pendente',
      dataVencimento: '2024-01-01',
      observacoes: 'Teste',
      usuario_id: 1
    }];

    dividasService = jasmine.createSpyObj('DividasService', ['listarDividas']);
    dividasService.listarDividas.and.returnValue(of(mockDividas));

    await TestBed.configureTestingModule({
      imports: [ListaDividasComponent, CommonModule],
      providers: [{ provide: DividasService, useValue: dividasService }]
    }).compileComponents();

    fixture = TestBed.createComponent(ListaDividasComponent);
    component = fixture.componentInstance;
    component.dividas = mockDividas;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
