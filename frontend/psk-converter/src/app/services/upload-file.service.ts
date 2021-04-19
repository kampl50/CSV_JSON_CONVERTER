import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ConvertRequest } from '../model.interface';

const PYTHON_API_UPLOAD_FILE = 'http://127.0.0.1:5000/parse';

@Injectable({
  providedIn: 'root',
})
export class UploadFileService {
  constructor(private httpClient: HttpClient) {}

  parseTable(converterRequest: ConvertRequest) {
    const formData: FormData = new FormData();
    formData.append('file', converterRequest.file, converterRequest.file.name);
    // todo: add settings object to request
    // formData.append('settings', converterRequest.settings)
    return this.httpClient.post(PYTHON_API_UPLOAD_FILE, formData);
  }
}
