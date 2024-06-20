import { Component, OnInit } from '@angular/core';
import { Abteilung, Job, MVApiClient, Mitarbeiter } from '../../../services/api';

@Component({
  selector: 'app-mitarbeiter',
  templateUrl: './mitarbeiter.component.html',
  styleUrl: './mitarbeiter.component.scss'
})
export class MitarbeiterComponent implements OnInit{
  private apiClient: MVApiClient;
  public mitarbeiter: Mitarbeiter[] = [];
  public jobs: Job[] = [];
  public abteilungen: Abteilung[] = [];


  constructor(apiClient: MVApiClient) {
    this.apiClient = apiClient;
  }

  getJobNameFromId(id: number): string {
    let job: Job | undefined =  this.jobs.find(job => job.id === id);
    return job ? job.titel : '';
  }

  getAbteilungNameFromId(id: number): string {
    console.log(this.abteilungen);
    console.log(id);
    let abteilung: Abteilung | undefined =  this.abteilungen.find(abteilung => abteilung.id === id);
    return abteilung ? abteilung.name : '';
  }

  ngOnInit(): void {
    this.apiClient.get_all_mitarbeiter().subscribe(mitarbeiter => {
      this.mitarbeiter = mitarbeiter;
      console.log(mitarbeiter)
    });
    this.apiClient.get_all_jobs().subscribe(jobs => {
      this.jobs = jobs;
    });
    this.apiClient.get_all_abteilungen().subscribe(abteilungen => {
      this.abteilungen = abteilungen;
      console.log(abteilungen);
    });
  }
}
