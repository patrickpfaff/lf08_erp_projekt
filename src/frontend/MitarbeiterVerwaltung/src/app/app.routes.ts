import { Routes } from '@angular/router';
import { MitarbeiterComponent } from './mitarbeiter/mitarbeiter.component';

export const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'mitarbeiter', component: MitarbeiterComponent },
];
