import { UploadFileService } from './../services/upload-file.service';
import { Component, OnInit } from '@angular/core';
import { ConvertRequest } from '../model.interface';

@Component({
  selector: 'app-converter-menu',
  templateUrl: './converter-menu.component.html',
  styleUrls: ['./converter-menu.component.css'],
})
export class ConverterMenuComponent implements OnInit {
  fileToUpload: File = null;

  formatFrom: string;
  formatTo: string;
  formats: string[] = ['CSV', 'JSON', 'XML'];
  formatsWithoutSelected: string[] = new Array();

  constructor(private uploadFileService: UploadFileService) {}

  ngOnInit(): void {}
  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }

  uploadFile() {
    let convertRequest: ConvertRequest = {
      file: this.fileToUpload,
      settings: {
        from: this.formatFrom,
        to: this.formatTo,
      },
    };
    this.uploadFileService.parseTable(convertRequest).subscribe((data: any) => {
      console.log(data);
    });
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
