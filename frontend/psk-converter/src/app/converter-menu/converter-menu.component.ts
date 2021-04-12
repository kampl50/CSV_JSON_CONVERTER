import { UploadFileService } from './../services/upload-file.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-converter-menu',
  templateUrl: './converter-menu.component.html',
  styleUrls: ['./converter-menu.component.css'],
})
export class ConverterMenuComponent implements OnInit {
  fileToUpload: File = null;
  formats: string[] = ['CSV', 'JSON', 'XML'];
  constructor(private uploadFileService: UploadFileService) {}

  ngOnInit(): void {}
  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }

  uploadFile() {
    this.uploadFileService
      .parseTable(this.fileToUpload)
      .subscribe((data: any) => {
        console.log(data);
      });
  }
}
