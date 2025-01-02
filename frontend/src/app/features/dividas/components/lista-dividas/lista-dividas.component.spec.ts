import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaDividasComponent } from './lista-dividas.component';

describe('ListaDividasComponent', () => {
  let component: ListaDividasComponent;
  let fixture: ComponentFixture<ListaDividasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaDividasComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListaDividasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
