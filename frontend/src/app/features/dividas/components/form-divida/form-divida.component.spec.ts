import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormDividaComponent } from './form-divida.component';

describe('FormDividaComponent', () => {
  let component: FormDividaComponent;
  let fixture: ComponentFixture<FormDividaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FormDividaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FormDividaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
