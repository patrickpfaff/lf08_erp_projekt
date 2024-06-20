import { Component } from '@angular/core';
import { Abteilung, Job, MVApiClient } from '../../../services/api';
import { FormControl, FormGroup } from '@angular/forms';
import { AnimationEvent } from '@angular/animations';
import { ToastrService } from 'ngx-toastr';

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
    strasse: new FormControl<string>(''),
    hausnummer: new FormControl<string>(''),
    plz: new FormControl<number>(0),
    zusatz: new FormControl<string>(''),
  });

  jobs: string[] = [];
  job_models: Job[] = [];
  options: string[] = [];
  departments: string[] = [];
  departments_models: Abteilung[] = [];
  toastr: ToastrService;

  constructor(apiClient: MVApiClient, toastr: ToastrService) {
    this.apiClient = apiClient;
    this.toastr = toastr;
  }

 
  onAbteilungDropDown($event: any) {
    this.apiClient.get_all_abteilungen().subscribe((data: Abteilung[]) => {
      this.departments = data.map((abteilung) => abteilung.name);
      this.departments_models = data;
      console.log(data);
    });
  }

  onJobDropDown($event: any) {
    this.apiClient.get_all_jobs().subscribe((data: Job[]) => {
      this.jobs = data.map((job) => job.titel);
      this.job_models = data;
      console.log(data);
    });
  }

  addMitarbeiter($event: any) {
    console.log($event);

    // Check vorname
    if (this.mitarbeiterForm.value.vorname === '' || this.mitarbeiterForm.value.vorname === null || this.mitarbeiterForm.value.vorname === undefined) {
      this.toastr.error('Vorname darf nicht leer sein', 'Fehler');
      return;
    }

    // Check nachname
    if (this.mitarbeiterForm.value.nachname === '' || this.mitarbeiterForm.value.nachname === null || this.mitarbeiterForm.value.nachname === undefined) {
      this.toastr.error('Nachname darf nicht leer sein', 'Fehler');
      return;
    }

    // Check abteilung
    if (this.mitarbeiterForm.value.abteilung === '' || this.mitarbeiterForm.value.abteilung === null || this.mitarbeiterForm.value.abteilung === undefined) {
      this.toastr.error('Abteilung darf nicht leer sein', 'Fehler');
      return;
    }

    // Check job
    if (this.mitarbeiterForm.value.job === '' || this.mitarbeiterForm.value.job === null || this.mitarbeiterForm.value.job === undefined) {
      this.toastr.error('Job darf nicht leer sein', 'Fehler');
      return;
    }

    // Check strasse
    if (this.mitarbeiterForm.value.strasse === '' || this.mitarbeiterForm.value.strasse === null || this.mitarbeiterForm.value.strasse === undefined) {
      this.toastr.error('Strasse darf nicht leer sein', 'Fehler');
      return;
    }

    // Check hausnummer
    if (this.mitarbeiterForm.value.hausnummer === '' || this.mitarbeiterForm.value.hausnummer === null || this.mitarbeiterForm.value.hausnummer === undefined) {
      this.toastr.error('Hausnummer darf nicht leer sein', 'Fehler');
      return;
    }

    // Check plz
    if (this.mitarbeiterForm.value.plz === 0 || this.mitarbeiterForm.value.plz === null || this.mitarbeiterForm.value.plz === undefined) {
      this.toastr.error('PLZ darf nicht leer sein', 'Fehler');
      return;
    }

    // Check geburtsdatum
    if (this.mitarbeiterForm.value.geburtsdatum === new Date() || this.mitarbeiterForm.value.geburtsdatum === null || this.mitarbeiterForm.value.geburtsdatum === undefined) {
      this.toastr.error('Geburtsdatum darf nicht leer sein', 'Fehler');
      return;
    }

    // Check angestelltSeit
    if (this.mitarbeiterForm.value.angestelltSeit === new Date() || this.mitarbeiterForm.value.angestelltSeit === null || this.mitarbeiterForm.value.angestelltSeit === undefined) {
      this.toastr.error('Angestellt seit darf nicht leer sein', 'Fehler');
      return;
    }

    // Check Zusatz
    if (this.mitarbeiterForm.value.zusatz === '' || this.mitarbeiterForm.value.zusatz === null || this.mitarbeiterForm.value.zusatz === undefined) {
      this.mitarbeiterForm.value.zusatz = '';
    }

    // Add Mitarbeiter

    // Get AbteilungId
    let abteilung: Abteilung | undefined = this.departments_models.find((abteilung) => abteilung.name === this.mitarbeiterForm.value.abteilung);
    if (abteilung === undefined || abteilung.id === undefined || abteilung.id === null) {
      this.toastr.error('Abteilung nicht gefunden', 'Fehler');
      return;
    }

    // Get JobId
    let job: Job | undefined = this.job_models.find((job) => job.titel === this.mitarbeiterForm.value.job);
    if (job === undefined || job.id === undefined || job.id === null) {
      this.toastr.error('Job nicht gefunden', 'Fehler');
      return;
    }

    this.apiClient.add_mitarbeiter(
      this.mitarbeiterForm.value.vorname,
      this.mitarbeiterForm.value.nachname,
      this.mitarbeiterForm.value.geburtsdatum.toString(),
      this.mitarbeiterForm.value.angestelltSeit.toString(),
      job.id,
      abteilung.id,
      this.mitarbeiterForm.value.strasse,
      this.mitarbeiterForm.value.hausnummer,
      this.mitarbeiterForm.value.plz.toString(),
      this.mitarbeiterForm.value.zusatz
    ).subscribe(() => {
      this.toastr.success('Mitarbeiter hinzugefügt', 'Erfolg');
    });
  }
}
