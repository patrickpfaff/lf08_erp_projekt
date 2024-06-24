import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'; // Add this line

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MitarbeiterComponent } from './components/mitarbeiter/mitarbeiter/mitarbeiter.component';
import { NavbarComponent } from './components/navigation/navbar/navbar.component';
import { HttpClient, HttpClientModule, provideHttpClient } from '@angular/common/http';
import { MVApiClient } from './services/api';
import { AddMitarbeiterComponent } from './components/mitarbeiter/add-mitarbeiter/add-mitarbeiter.component';
import { FormGroup, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BadgeModule } from 'primeng/badge';
import { MenubarModule } from 'primeng/menubar';
import { InputTextareaModule } from 'primeng/inputtextarea';
import { MenuModule } from 'primeng/menu';
import { AvatarModule } from 'primeng/avatar';
import { RouterLink } from '@angular/router';
import { ButtonModule } from 'primeng/button';
import { InputNumberModule } from 'primeng/inputnumber';
import { InputTextModule } from 'primeng/inputtext';
import { DropdownModule } from 'primeng/dropdown';
import { Calendar, CalendarModule } from 'primeng/calendar';
import { ToastrModule } from 'ngx-toastr';
import { TableModule } from 'primeng/table';
import { EditmitarbeiterComponent } from './components/mitarbeiter/editmitarbeiter/editmitarbeiter.component';
import { JobsComponent } from './components/jobs/jobs/jobs.component';
import { AddJobComponent } from './components/jobs/add-job/add-job.component';
import { EditJobComponent } from './components/jobs/edit-job/edit-job.component';
import { AbteilungenComponent } from './components/abteilungen/abteilungen/abteilungen.component';
import { AddAbteilungComponent } from './components/abteilungen/add-abteilung/add-abteilung.component';
import { EditAbteilungComponent } from './components/abteilungen/edit-abteilung/edit-abteilung.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    MitarbeiterComponent,
    NavbarComponent,
    AddMitarbeiterComponent,
    EditmitarbeiterComponent,
    JobsComponent,
    AddJobComponent,
    EditJobComponent,
    AbteilungenComponent,
    AddAbteilungComponent,
    EditAbteilungComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    ButtonModule,
    ReactiveFormsModule,
    AppRoutingModule,
    RouterLink,
    HttpClientModule,
    FormsModule,
    MenubarModule,
    MenuModule,
    BadgeModule,
    InputTextareaModule,
    InputNumberModule,
    InputTextModule,
    CalendarModule,
    DropdownModule,
    TableModule,
    ToastrModule.forRoot(),
    AvatarModule,
  ],
  providers: [
    provideHttpClient(),
    { provide: 'API_BASE_URL', useValue: 'http://localhost:8000' },
    { provide: MVApiClient, useClass: MVApiClient, deps: [HttpClient, 'API_BASE_URL']}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
