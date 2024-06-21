import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MitarbeiterComponent } from './components/mitarbeiter/mitarbeiter/mitarbeiter.component';
import { AddMitarbeiterComponent } from './components/mitarbeiter/add-mitarbeiter/add-mitarbeiter.component';
import { EditmitarbeiterComponent } from './components/mitarbeiter/editmitarbeiter/editmitarbeiter.component';
import { JobsComponent } from './components/jobs/jobs/jobs.component';
import { AddJobComponent } from './components/jobs/add-job/add-job.component';
import { EditJobComponent } from './components/jobs/edit-job/edit-job.component';

const routes: Routes = [
  { path: 'mitarbeiter', component:MitarbeiterComponent, pathMatch: 'full' },
  { path: 'addmitarbeiter', component:AddMitarbeiterComponent, pathMatch: 'full' },
  { path: 'mitarbeiter/edit/:id', component:EditmitarbeiterComponent, pathMatch: 'full' },
  { path: 'jobs', component: JobsComponent, pathMatch: 'full' },
  { path: 'addjob', component: AddJobComponent, pathMatch: 'full' },
  { path: 'jobs/edit/:id', component: EditJobComponent, pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
