import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';

import { MatToolbarModule } from '@angular/material/toolbar';
import { ConverterMenuComponent } from './converter-menu/converter-menu.component';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatRadioModule } from '@angular/material/radio';
import { MatSelectModule } from '@angular/material/select';

import { AppComponent } from './app.component';
import { NgxMatFileInputModule } from '@angular-material-components/file-input';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { UploadFileService } from './services/upload-file.service';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { MaterialFileInputModule } from 'ngx-material-file-input';

@NgModule({
  declarations: [AppComponent, ConverterMenuComponent],
  imports: [
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatSelectModule,
    MatDatepickerModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatRadioModule,
    MatSelectModule,
    MatCheckboxModule,
    MatIconModule,
    MatCardModule,
    HttpClientModule,
    MaterialFileInputModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
