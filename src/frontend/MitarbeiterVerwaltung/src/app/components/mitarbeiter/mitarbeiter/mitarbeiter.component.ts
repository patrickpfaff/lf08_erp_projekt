import { Component, OnInit } from '@angular/core';
import { MVApiClient } from '../../../services/api';

@Component({
  selector: 'app-mitarbeiter',
  templateUrl: './mitarbeiter.component.html',
  styleUrl: './mitarbeiter.component.scss'
})
export class MitarbeiterComponent implements OnInit{
  private apiClient: MVApiClient;

  constructor(apiClient: MVApiClient) {
    this.apiClient = apiClient;
  }

  ngOnInit(): void {
    this.apiClient.get_all_mitarbeiter().subscribe(mitarbeiter => {
      console.log(mitarbeiter);
    });
  }
}
