import { UploadFileService } from './../services/upload-file.service';
import { Component, OnInit } from '@angular/core';
import { ConvertRequest } from '../model.interface';
import { DownloadFileService } from '../services/download-file.service';
import { saveAs } from 'file-saver';
import { HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-converter-menu',
  templateUrl: './converter-menu.component.html',
  styleUrls: ['./converter-menu.component.css'],
})
export class ConverterMenuComponent implements OnInit {
  fileToUpload: File = null;
  filenameToDownLoad = '';

  formatFrom: string = '';
  formatTo: string = '';
  formats: string[] = ['CSV', 'JSON', 'XML'];
  separators: string[] = ['.', ',', ';', '|', '\\t'];
  selectedSeparator: string = null;
  formatsWithoutSelected: string[] = new Array();

  isFailedFormat: boolean = false;
  isFailedFromFormat: boolean = false;
  isFailedToFormat: boolean = false;
  isFailedFile: boolean = false;

  constructor(
    private uploadFileService: UploadFileService,
    private downloadFileService: DownloadFileService
  ) {}

  ngOnInit(): void {}
  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }

  downloadFile() {
    const EXT = this.filenameToDownLoad.substr(
      this.filenameToDownLoad.lastIndexOf('.') + 1
    );
    this.downloadFileService
      .downloadFile({ fileName: this.filenameToDownLoad })
      .subscribe((data) => {
        //save it on the client machine.
        saveAs(
          new Blob([data], { type: MIME_TYPES[EXT] }),
          this.filenameToDownLoad
        );
      });
  }

  uploadFile() {
    if (this.fileToUpload === null) {
      this.isFailedFile = true;

      setTimeout(() => (this.isFailedFile = false), 3000);
      return;
    }
    const fileFormat = this.fileToUpload.name.split('.')[1].toUpperCase();
    if (fileFormat !== this.formatFrom) {
      this.isFailedFormat = true;

      setTimeout(() => (this.isFailedFormat = false), 3000);
      return;
    }

    if (this.formatFrom === '') {
      this.isFailedFromFormat = true;

      setTimeout(() => (this.isFailedFromFormat = false), 3000);
      return;
    }

    if (this.formatTo === '') {
      this.isFailedToFormat = true;

      setTimeout(() => (this.isFailedToFormat = false), 3000);
      return;
    }

    let convertRequest: ConvertRequest = {
      file: this.fileToUpload,
      settings: {
        from: this.formatFrom,
        to: this.formatTo,
        separator: this.selectedSeparator,
      },
    };
    this.uploadFileService.parseTable(convertRequest).subscribe(
      (result) => console.log(result, 'jestem result'),
      (error) => {
        this.filenameToDownLoad = error.error.text;
      }
    );
  }

  setListFormatsTo(value: string) {
    let newArray = [...this.formats];

    newArray = this.filterAccesFormatters(value, newArray);
    this.formatsWithoutSelected = newArray;
    this.formatFrom = value;
    this.formatTo = '';
  }

  private filterAccesFormatters(
    value: string,
    formatters: Array<string>
  ): Array<string> {
    let index = formatters.indexOf(value);
    if (index > -1) {
      formatters.splice(index, 1);
    }
    if (value === 'JSON') {
      index = formatters.indexOf('XML');
      formatters.splice(index, 1);
    }
    if (value === 'XML') {
      index = formatters.indexOf('JSON');
      formatters.splice(index, 1);
    }
    return formatters;
  }

  setFormatTo(value: string) {
    this.formatTo = value;
  }

  setSeparator(value: string) {
    this.selectedSeparator = value;
  }
}

const MIME_TYPES = {
  pdf: 'application/pdf',
  xls: 'application/vnd.ms-excel',
  xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetxml.sheet',
};
