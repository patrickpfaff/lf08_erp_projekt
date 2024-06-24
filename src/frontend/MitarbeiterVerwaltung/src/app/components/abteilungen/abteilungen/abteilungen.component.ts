import { Component, OnInit } from '@angular/core';
import { Abteilung, MVApiClient, Mitarbeiter } from '../../../services/api';
import { Router } from '@angular/router';
import { TableRowSelectEvent } from 'primeng/table';
import { FormGroup, FormControl } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-abteilungen',
  templateUrl: './abteilungen.component.html',
  styleUrl: './abteilungen.component.scss'
})
export class AbteilungenComponent implements OnInit{
  public abteilungen: Abteilung[] = [];
  public selectedAbteilung: Abteilung | undefined;
  public currentLeiter: Mitarbeiter | undefined;
  public currentLeiterJob: string = '';

  constructor(private apiClient: MVApiClient, private router: Router, private toastr: ToastrService) { }

  ngOnInit(): void {
    this.apiClient.get_all_abteilungen().subscribe(abteilungen => {
      this.abteilungen = abteilungen;
    });
  }

  onRowSelect($event: TableRowSelectEvent) {
    if (this.selectedAbteilung) {

      if (this.selectedAbteilung.leiterId) {
        this.apiClient.get_mitarbeiter_by_id(this.selectedAbteilung.leiterId).subscribe(leiter => {
          this.currentLeiter = leiter;

          this.apiClient.get_job_by_id(leiter.jobId).subscribe(job => {
            this.currentLeiterJob = job.titel;
          });
        });
      }
    }
  }

  onEditAbteilung() {
    console.log(this.selectedAbteilung);
    if (this.selectedAbteilung) {
      this.router.navigate(['/abteilungen/edit', this.selectedAbteilung.id]);
    }
  }

  onDeleteAbteilung() {
    if (this.selectedAbteilung !== undefined && this.selectedAbteilung.id !== undefined) {
      this.apiClient.delete_abteilung(this.selectedAbteilung.id).subscribe(() => {
        this.apiClient.get_all_abteilungen().subscribe(abteilungen => {
          this.toastr.success('Abteilung gelöscht', 'Erfolg');
          this.abteilungen = abteilungen;
        });
      });
    }
      else {
        this.toastr.error('Fehler beim Löschen der Abteilung', 'Fehler');
        console.log('current id');
        console.log(this.selectedAbteilung?.id);
        console.log(this.selectedAbteilung);
      }
    
    }
  }

