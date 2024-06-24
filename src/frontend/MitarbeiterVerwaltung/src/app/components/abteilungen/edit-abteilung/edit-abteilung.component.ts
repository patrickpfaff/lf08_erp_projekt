import { AnimationEvent } from '@angular/animations';
import { Component, OnInit } from '@angular/core';
import { Abteilung, MVApiClient, Mitarbeiter } from '../../../services/api';
import { ToastrService } from 'ngx-toastr';
import { ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-edit-abteilung',
  templateUrl: './edit-abteilung.component.html',
  styleUrl: './edit-abteilung.component.scss'
})
export class EditAbteilungComponent implements OnInit {
  keinLeiter: string = 'Kein Abteilungsleiter';
  leiter: string = '';
  mitarbeiter: string[] = [];
  mitarbeiter_models: Mitarbeiter[] = [];
  current_abteilung: Abteilung | undefined;
  beschreibung: string = '';
  id: number | undefined;
  name: string = '';

  constructor(private apiClient: MVApiClient, private toastr: ToastrService, private route: ActivatedRoute) { }

  onLeiterDropDown($event: AnimationEvent) {
    this.updateMitarbeiter();
  }

  saveChanges($event: MouseEvent) {
    
    console.log('updateMitarbeiter');
    if (this.name === '' || this.beschreibung === '' || !this.name || !this.beschreibung) {
      this.toastr.error('Bitte füllen Sie alle Felder aus', 'Fehler');
      return;
    }

    let leiterId: number | undefined;
    if (this.leiter === this.keinLeiter) {
      leiterId = undefined;
      console.log("leiterid set to undefined")
    } else {
      leiterId = this.mitarbeiter_models.find(m => `${m.vorname} ${m.nachname}` === this.leiter)?.id;
      console.log("leiterid set to " + leiterId)
    }
    if (this.id !== undefined && this.id !== null) {
      console.log('updateMitarbeiter2');
      this.apiClient.update_abteilung(this.id, this.name, this.beschreibung, leiterId).subscribe(() => {
        this.toastr.success('Änderungen gespeichert', 'Erfolg');
        console.log('updateMitarbeiter3');
      }), () => {
        this.toastr.error('Fehler beim Speichern der Änderungen', 'Fehler');
      };
    }
    else {
      this.toastr.error('Fehler beim Speichern der Änderungen', 'Fehler');
      console.log('current id');
      console.log(this.id);
    }
  }

  ngOnInit(): void {
    this.updateMitarbeiter();
    this.route.paramMap.subscribe((params: ParamMap) => {
      console.log("getting abteilung by id");
      this.apiClient.get_abteilung_by_id(+params.get('id')!).subscribe(abteilung => {
        console.log("response from get_abteilung_by_id");
        this.id = +params.get('id')!;
        console.log(this.id);
        this.current_abteilung = abteilung;
        this.name = abteilung.name;
        this.beschreibung = abteilung.beschreibung;
        if (abteilung.leiterId) {
          this.apiClient.get_mitarbeiter_by_id(abteilung.leiterId).subscribe(leiter => {
            this.leiter = `${leiter.vorname} ${leiter.nachname}`;
          });
        } else {
          this.leiter = this.keinLeiter;
        }
      });  
    });
  }
  

  updateMitarbeiter(): void {
    this.apiClient.get_all_mitarbeiter().subscribe(mitarbeiter => {
      this.mitarbeiter_models = mitarbeiter.filter(m => m.abteilungId === this.id);
      this.mitarbeiter = mitarbeiter.filter(m => m.abteilungId === this.id).map(m => `${m.vorname} ${m.nachname}`);
      this.mitarbeiter.unshift(this.keinLeiter);
      console.log(this.mitarbeiter_models);
      console.log(this.mitarbeiter);
    });
  }
}
