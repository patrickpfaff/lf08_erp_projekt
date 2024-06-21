import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Job, MVApiClient } from '../../../services/api';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-add-job',
  templateUrl: './add-job.component.html',
  styleUrl: './add-job.component.scss'
})
export class AddJobComponent implements OnInit{
  jobs: Job[] = [];

  addJobForm = new FormGroup({
    jobname: new FormControl<string>(''),
  });

  constructor(private apiClient: MVApiClient, private toastr: ToastrService) { }

  ngOnInit(): void {
    this.apiClient.get_all_jobs().subscribe(jobs => {
      this.jobs = jobs;
    });
  }

  addJob($event: any) {
    if (!this.addJobForm.valid || this.addJobForm.value.jobname === '' || !this.addJobForm.value.jobname) {
      this.toastr.error('Jobtitel darf nicht leer sein!');
      return;
    }

    if (this.jobs.some(job => job.titel === this.addJobForm.value.jobname)) {
      this.toastr.error('Jobtitel existiert bereits!');
      return;
    }

    // this.jobs.some(job => job.titel === this.addJobForm.value.jobname)
    this.apiClient.add_job(this.addJobForm.value.jobname).subscribe(job => {
      this.jobs.push(job);
      this.toastr.success('Job hinzugefügt!');
      this.addJobForm.reset();
    });
  }
}
