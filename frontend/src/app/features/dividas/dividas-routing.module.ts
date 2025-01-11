import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListaDividasComponent } from './components/lista-dividas/lista-dividas.component';
import { CriarDividaComponent } from './components/criar-divida/criar-divida.component';
import { EditarDividaComponent } from './components/editar-divida/editar-divida.component';

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: '',
        component: ListaDividasComponent
      },
      {
        path: 'criar',
        component: CriarDividaComponent
      },
      {
        path: ':id/editar',
        component: EditarDividaComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DividasRoutingModule { }
