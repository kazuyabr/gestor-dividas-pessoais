import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DividasRoutingModule } from './dividas-routing.module';
import { ListaDividasComponent } from './components/lista-dividas/lista-dividas.component';
import { CriarDividaComponent } from './components/criar-divida/criar-divida.component';
import { EditarDividaComponent } from './components/editar-divida/editar-divida.component';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    ListaDividasComponent,
    CriarDividaComponent,
    EditarDividaComponent
  ],
  imports: [
    CommonModule,
    DividasRoutingModule,
    ReactiveFormsModule
  ]
})
export class DividasModule { }
