import { Component } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent {
  public items: MenuItem[];

  constructor() {
    this.items = [
      { 
        label: 'Home',
        url: 'home'
      },
      {
        label: 'Mitarbeiter',
        url: 'mitarbeiter'
      },
      {
        label: 'Jobs',
        url: 'jobs'
      },
      {
        label: 'Abteilungen',
        url: 'abteilungen'
      }
    ];
  }
}
