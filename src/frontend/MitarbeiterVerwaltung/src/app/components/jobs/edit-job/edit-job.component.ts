import { Component, OnInit } from '@angular/core';
import { Job, MVApiClient } from '../../../services/api';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-edit-job',
  templateUrl: './edit-job.component.html',
  styleUrl: './edit-job.component.scss'
})
export class EditJobComponent implements OnInit{
  jobname?: string;
  job?: Job;

  constructor(private apiClient: MVApiClient, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      let jobId = Number(params.get('id'));
      this.apiClient.get_job_by_id(jobId).subscribe(job => {
        this.job = job
      });
      this.jobname = this.job!.titel!;
    });
  }

  saveChanges($event: MouseEvent) {
    // if (this.job) {
    //   this.apiClient.update_job(this.job).subscribe(() => {
    //     console.log('Job updated');
    //   });
    // }
  }

}
