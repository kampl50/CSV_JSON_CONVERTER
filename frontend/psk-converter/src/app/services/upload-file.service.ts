import { HttpClient, HttpParams } from '@angular/common/http';
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
    let params = new HttpParams();
    params = params.append('from', converterRequest.settings.from);
    params = params.append('to', converterRequest.settings.to);
    params = params.append('separator', converterRequest.settings.separator);
    console.log(params);
    return this.httpClient.post(PYTHON_API_UPLOAD_FILE, formData, {
      params: params,
    });
  }
}
