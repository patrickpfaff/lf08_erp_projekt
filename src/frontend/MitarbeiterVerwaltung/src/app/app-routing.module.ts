import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MitarbeiterComponent } from './components/mitarbeiter/mitarbeiter/mitarbeiter.component';
import { AddMitarbeiterComponent } from './components/mitarbeiter/add-mitarbeiter/add-mitarbeiter.component';
import { EditmitarbeiterComponent } from './components/mitarbeiter/editmitarbeiter/editmitarbeiter.component';
import { JobsComponent } from './components/jobs/jobs/jobs.component';
import { AddJobComponent } from './components/jobs/add-job/add-job.component';
import { EditJobComponent } from './components/jobs/edit-job/edit-job.component';
import { AbteilungenComponent } from './components/abteilungen/abteilungen/abteilungen.component';
import { AddAbteilungComponent } from './components/abteilungen/add-abteilung/add-abteilung.component';
import { EditAbteilungComponent } from './components/abteilungen/edit-abteilung/edit-abteilung.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  { path: 'mitarbeiter', component:MitarbeiterComponent, pathMatch: 'full' },
  { path: 'mitarbeiter/add', component:AddMitarbeiterComponent, pathMatch: 'full' },
  { path: 'mitarbeiter/edit/:id', component:EditmitarbeiterComponent, pathMatch: 'full' },
  { path: 'jobs', component: JobsComponent, pathMatch: 'full' },
  { path: 'addjob', component: AddJobComponent, pathMatch: 'full' },
  { path: 'jobs/edit/:id', component: EditJobComponent, pathMatch: 'full' },
  { path: 'abteilungen', component: AbteilungenComponent, pathMatch: 'full' },
  { path: 'abteilungen/add', component: AddAbteilungComponent, pathMatch: 'full' },
  { path: 'abteilungen/edit/:id', component: EditAbteilungComponent, pathMatch: 'full'},
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent, pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
