import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditAbteilungComponent } from './edit-abteilung.component';

describe('EditAbteilungComponent', () => {
  let component: EditAbteilungComponent;
  let fixture: ComponentFixture<EditAbteilungComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EditAbteilungComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditAbteilungComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
