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

  formatFrom: string;
  formatTo: string;
  formats: string[] = ['CSV', 'JSON', 'XML'];
  formatsWithoutSelected: string[] = new Array();

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
    let convertRequest: ConvertRequest = {
      file: this.fileToUpload,
      settings: {
        from: this.formatFrom,
        to: this.formatTo,
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
    const index = newArray.indexOf(value);

    if (index > -1) {
      newArray.splice(index, 1);
    }
    this.formatsWithoutSelected = newArray;
    this.formatFrom = value;
  }

  setFormatTo(value: string) {
    this.formatTo = value;
  }
}

const MIME_TYPES = {
  pdf: 'application/pdf',
  xls: 'application/vnd.ms-excel',
  xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetxml.sheet',
};
