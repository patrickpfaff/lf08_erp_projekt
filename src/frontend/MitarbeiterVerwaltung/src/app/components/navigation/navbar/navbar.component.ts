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
        url: ''
      },
      {
        label: 'Mitarbeiter',
        url: 'mitarbeiter'
      },
      {
        label: 'Mitarbeiter hinzufügen',
        url: 'addmitarbeiter'
      }
    ];
  }
}
