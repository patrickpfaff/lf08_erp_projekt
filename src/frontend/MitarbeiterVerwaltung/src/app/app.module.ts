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

@NgModule({
  declarations: [
    AppComponent,
    MitarbeiterComponent,
    NavbarComponent,
    AddMitarbeiterComponent
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
