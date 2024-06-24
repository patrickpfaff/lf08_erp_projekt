import { Component, OnInit } from '@angular/core';
import { Job, MVApiClient } from '../../../services/api';
import { TableRowSelectEvent } from 'primeng/table';
import { Router } from '@angular/router';

@Component({
  selector: 'app-jobs',
  templateUrl: './jobs.component.html',
  styleUrl: './jobs.component.scss'
})
export class JobsComponent implements OnInit{

  jobs_models: Job[] = [];
  selectedJob?: Job;

  constructor(private apiClient: MVApiClient, private router: Router) {}

  ngOnInit(): void {
    this.apiClient.get_all_jobs().subscribe(jobs => {
      this.jobs_models = jobs;
    });
  }

  onEditJob() {
    if (this.selectedJob) {
      this.router.navigate(['/jobs/edit', this.selectedJob.id]);
    }
  }

  onRowSelect($event: TableRowSelectEvent) {
  }

  onDeleteJob() {
    if (this.selectedJob && this.selectedJob.id) {
      this.apiClient.delete_job(this.selectedJob.id).subscribe(() => {
        this.apiClient.get_all_jobs().subscribe(jobs => {
          this.jobs_models = jobs;
        });
      });
    }
  }
}
