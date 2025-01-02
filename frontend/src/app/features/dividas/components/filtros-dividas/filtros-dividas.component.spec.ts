import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FiltrosDividasComponent } from './filtros-dividas.component';

describe('FiltrosDividasComponent', () => {
  let component: FiltrosDividasComponent;
  let fixture: ComponentFixture<FiltrosDividasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FiltrosDividasComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FiltrosDividasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
