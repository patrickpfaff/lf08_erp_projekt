import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddAbteilungComponent } from './add-abteilung.component';

describe('AddAbteilungComponent', () => {
  let component: AddAbteilungComponent;
  let fixture: ComponentFixture<AddAbteilungComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AddAbteilungComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AddAbteilungComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
