import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MitarbeiterComponent } from './components/mitarbeiter/mitarbeiter/mitarbeiter.component';
import { AddMitarbeiterComponent } from './components/mitarbeiter/add-mitarbeiter/add-mitarbeiter.component';

const routes: Routes = [
  { path: 'mitarbeiter', component:MitarbeiterComponent, pathMatch: 'full' },
  { path: 'addmitarbeiter', component:AddMitarbeiterComponent, pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
