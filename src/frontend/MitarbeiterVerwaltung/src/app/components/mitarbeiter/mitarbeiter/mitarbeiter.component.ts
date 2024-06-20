import { Component, OnInit } from '@angular/core';
import { Abteilung, Adresse, Job, MVApiClient, Mitarbeiter } from '../../../services/api';
import { TableRowSelectEvent } from 'primeng/table';

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
  public selectedMitarbeiter: Mitarbeiter | undefined;
  public curAdresse: Adresse | undefined;
  public curOrt: string = '';

  constructor(apiClient: MVApiClient) {
    this.apiClient = apiClient;
  }

  getJobNameFromId(id: number): string {
    let job: Job | undefined =  this.jobs.find(job => job.id === id);
    return job ? job.titel : '';
  }

  getAbteilungNameFromId(id: number): string {
    let abteilung: Abteilung | undefined =  this.abteilungen.find(abteilung => abteilung.id === id);
    return abteilung ? abteilung.name : '';
  }

  ngOnInit(): void {
    this.apiClient.get_all_mitarbeiter().subscribe(mitarbeiter => {
      this.mitarbeiter = mitarbeiter;
    });
    this.apiClient.get_all_jobs().subscribe(jobs => {
      this.jobs = jobs;
    });
    this.apiClient.get_all_abteilungen().subscribe(abteilungen => {
      this.abteilungen = abteilungen;
    });
  }

  onRowSelect($event: TableRowSelectEvent) {
    if (this.selectedMitarbeiter && this.selectedMitarbeiter.adresseId) {
      this.apiClient.get_adresse_by_id(this.selectedMitarbeiter.adresseId).subscribe(adresse => {
        this.curAdresse = adresse;

        this.apiClient.get_ortsname_from_plz(adresse.plz).subscribe(ort => {
          this.curOrt = ort;
        });
      });
    }
  }
}
