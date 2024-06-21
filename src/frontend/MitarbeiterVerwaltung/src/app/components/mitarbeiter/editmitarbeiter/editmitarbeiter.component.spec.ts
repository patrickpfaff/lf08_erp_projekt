import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditmitarbeiterComponent } from './editmitarbeiter.component';

describe('EditmitarbeiterComponent', () => {
  let component: EditmitarbeiterComponent;
  let fixture: ComponentFixture<EditmitarbeiterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EditmitarbeiterComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditmitarbeiterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
