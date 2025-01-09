import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FormDividaComponent } from './form-divida.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { CommonModule } from '@angular/common';

describe('FormDividaComponent', () => {
  let component: FormDividaComponent;
  let fixture: ComponentFixture<FormDividaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        FormDividaComponent,
        ReactiveFormsModule,
        HttpClientTestingModule,
        RouterTestingModule,
        CommonModule
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(FormDividaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
