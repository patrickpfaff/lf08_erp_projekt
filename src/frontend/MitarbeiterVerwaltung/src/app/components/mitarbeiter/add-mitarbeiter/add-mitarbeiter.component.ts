import { Component } from '@angular/core';
import { Abteilung, Job, MVApiClient } from '../../../services/api';
import { FormControl, FormGroup } from '@angular/forms';
import { AnimationEvent } from '@angular/animations';

@Component({
  selector: 'app-add-mitarbeiter',
  templateUrl: './add-mitarbeiter.component.html',
  styleUrl: './add-mitarbeiter.component.scss'
})
export class AddMitarbeiterComponent {
  private apiClient: MVApiClient;

  mitarbeiterForm = new FormGroup({
    vorname: new FormControl<string>(''),
    nachname: new FormControl<string>(''),
    abteilung: new FormControl<string>(''),
    geburtsdatum: new FormControl<Date>(new Date()),
    angestelltSeit: new FormControl<Date>(new Date()),
    job: new FormControl<string>(''),
  });

  jobs: string[] = [];
  options: string[] = [];
  departments: string[] = [];

  constructor(apiClient: MVApiClient) {
    this.apiClient = apiClient;
  }

 
  onAbteilungDropDown($event: any) {
    this.apiClient.get_all_abteilungen().subscribe((data: Abteilung[]) => {
      this.departments = data.map((abteilung) => abteilung.name);
      console.log(data);
    });
  }

  onJobDropDown($event: any) {
    this.apiClient.get_all_jobs().subscribe((data: Job[]) => {
      this.jobs = data.map((job) => job.titel);
      console.log(data);
    });
  }

  addMitarbeiter($event: any) {
    throw new Error('Method not implemented.');
  }
}
