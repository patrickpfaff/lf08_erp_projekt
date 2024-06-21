import { Component, OnInit } from '@angular/core';
import { Abteilung, Job, MVApiClient, Mitarbeiter } from '../../../services/api';
import { AnimationEvent } from '@angular/animations';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-editmitarbeiter',
  templateUrl: './editmitarbeiter.component.html',
  styleUrl: './editmitarbeiter.component.scss'
})
export class EditmitarbeiterComponent implements OnInit{
  mitarbeiterModels?: Mitarbeiter;
  vorname?: string;
  nachname?: string;
  geburtsdatum?: Date;
  angestelltSeit?: Date;
  strasse?: string;
  hausnummer?: string;
  plz?: string;
  zusatz?: string;
  abteilung?: string;
  job?: string;

  jobs_models: Job[] = [];
  jobs: string[] = [];
  abteilungen_models: Abteilung[] = [];
  abteilungen: string[] = [];

  apiService: MVApiClient;
  id?: number;

  constructor(apiService: MVApiClient, private route: ActivatedRoute, private toastr: ToastrService) {
    this.apiService = apiService;
  }

  ngOnInit() {
    this.route.paramMap.subscribe((params: ParamMap) => {
      this.id = +params.get('id')!;
    });
    
    this.apiService.get_all_jobs().subscribe(jobs => {
      this.jobs_models = jobs;
      this.jobs = jobs.map(job => job.titel);
    });

    this.apiService.get_all_abteilungen().subscribe(abteilungen => {
      this.abteilungen_models = abteilungen;
      this.abteilungen = abteilungen.map(abteilung => abteilung.name);
    });

    if (this.id) {
      this.apiService.get_mitarbeiter_by_id(this.id).subscribe(mitarbeiter => {
        console.log(mitarbeiter);
        this.vorname = mitarbeiter.vorname;
        this.nachname = mitarbeiter.nachname;
        this.geburtsdatum = new Date(mitarbeiter.geburtsdatum);
        this.angestelltSeit = new Date(mitarbeiter.angestelltseit);

        this.apiService.get_adresse_by_id(mitarbeiter.adresseId).subscribe(adresse => {
          this.strasse = adresse.strasse;
          this.hausnummer = adresse.hausnummer;
          this.plz = adresse.plz;
          this.zusatz = adresse.zusatz;
        });
  
        this.apiService.get_job_by_id(mitarbeiter.jobId).subscribe(job => {
          this.job = job.titel;
          console.log(job);
        });
  
        this.apiService.get_abteilung_by_id(mitarbeiter.abteilungId).subscribe(abteilung => {
          this.abteilung = abteilung.name;
        });
      });
    }
  }

  saveChanges($event: MouseEvent) {
    if (
      !this.id ||
      !this.vorname ||
      !this.nachname ||
      !this.geburtsdatum ||
      !this.angestelltSeit ||
      !this.strasse ||
      !this.hausnummer ||
      !this.plz ||
      !this.zusatz ||
      !this.abteilung ||
      !this.job
    ){
      this.toastr.error('Bitte füllen Sie alle Felder aus');
      return;
    }

    this.apiService.update_mitarbeiter(
      this.id,
      this.vorname,
      this.nachname,
      this.geburtsdatum.toString(),
      this.angestelltSeit.toString(),
      this.jobs_models.find(job => job.titel === this.job)!.id!,
      this.abteilungen_models.find(abteilung => abteilung.name === this.abteilung)!.id!,
      this.strasse,
      this.hausnummer,
      this.zusatz,
      this.plz
    ).subscribe(() => {
      this.toastr.success('Mitarbeiter erfolgreich aktualisiert');
    });
  }

  onAbteilungDropDown($event: any) {
    this.apiService.get_all_abteilungen().subscribe((data: Abteilung[]) => {
      this.abteilungen = data.map((abteilung) => abteilung.name);
      this.abteilungen_models = data;
      console.log(data);
    });
  }

  onJobDropDown($event: any) {
    this.apiService.get_all_jobs().subscribe((data: Job[]) => {
      this.jobs = data.map((job) => job.titel);
      this.jobs_models = data;
      console.log(data);
    });
  }
}
