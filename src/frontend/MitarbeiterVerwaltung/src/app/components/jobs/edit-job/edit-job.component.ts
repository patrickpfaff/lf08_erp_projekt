import { Component, OnInit } from '@angular/core';
import { Job, MVApiClient } from '../../../services/api';
import { ActivatedRoute } from '@angular/router';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-edit-job',
  templateUrl: './edit-job.component.html',
  styleUrl: './edit-job.component.scss'
})
export class EditJobComponent implements OnInit{
  jobname?: string;
  job?: Job;
  jobId: number | undefined;
  constructor(private apiClient: MVApiClient, private route: ActivatedRoute, private toastr: ToastrService) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      let jobId = Number(params.get('id'));
      this.jobId = jobId;
      this.apiClient.get_job_by_id(jobId).subscribe(job => {
        this.job = job

        this.jobname = job.titel;
      });
    });
  }

  saveChanges($event: MouseEvent) {
    if (this.jobname == "" || this.jobname == undefined) {
      this.toastr.error('Jobname darf nicht leer sein');
      return;
    }

    if (this.job && this.jobId) {
      this.apiClient.update_job(this.jobId, this.jobname).subscribe(() => {
        console.log('Job updated');
        this.toastr.success('Job erfolgreich aktualisiert');
      });
    }
  }

}
