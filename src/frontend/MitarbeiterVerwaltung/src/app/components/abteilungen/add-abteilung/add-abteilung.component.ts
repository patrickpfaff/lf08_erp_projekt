import { AnimationEvent } from '@angular/animations';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { MVApiClient, Mitarbeiter } from '../../../services/api';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-add-abteilung',
  templateUrl: './add-abteilung.component.html',
  styleUrl: './add-abteilung.component.scss'
})
export class AddAbteilungComponent implements OnInit{
  mitarbeiter: string[] = [];
  mitarbeiter_models: Mitarbeiter[] = [];
  keinLeiter: string = "Kein Abteilungsleiter";

  public abteilungForm = new FormGroup({
    name: new FormControl<string>(''),
    beschreibung: new FormControl<string>(''),
    leiter: new FormControl<string>(''),
  });

  constructor(private apiClient: MVApiClient, private toastr: ToastrService) { }

  onAbteilungenDropDown($event: AnimationEvent) {
    this.ngOnInit();
  }

  ngOnInit(): void {
    this.apiClient.get_all_mitarbeiter().subscribe(mitarbeiter => {
      this.mitarbeiter_models = mitarbeiter;
      this.mitarbeiter = mitarbeiter.map(m => `${m.vorname} ${m.nachname}`);
      this.mitarbeiter.unshift(this.keinLeiter)
    });
  }

  addAbteilung() {
    let leiterId: number | undefined;
    if (this.abteilungForm.value.leiter === this.keinLeiter) {
     leiterId = undefined;
    } else {
      leiterId = this.mitarbeiter_models.find(m => `${m.vorname} ${m.nachname}` === this.abteilungForm.get('leiter')?.value)?.id;
    }

    if (this.abteilungForm.value.beschreibung === null ||
      this.abteilungForm.value.beschreibung === undefined ||
      this.abteilungForm.value.beschreibung === '' ||
      this.abteilungForm.value.name === null ||
      this.abteilungForm.value.name === undefined ||
      this.abteilungForm.value.name === ''
    ) {
      this.toastr.error('Bitte füllen Sie alle Felder aus', 'Fehler');
      return;
    }

    this.apiClient.add_abteilung(
      this.abteilungForm.value.beschreibung,
      this.abteilungForm.value.name,
      leiterId,
      undefined
    ).subscribe(() => {
      this.toastr.success('Abteilung erfolgreich hinzugefügt', 'Erfolg');
    }, () => {
      this.toastr.error('Fehler beim Hinzufügen der Abteilung', 'Fehler');
    });


  }
}
