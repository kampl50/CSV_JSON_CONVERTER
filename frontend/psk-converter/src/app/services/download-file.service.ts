import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';

const PYTHON_API_DOWNLOAD_FILE = 'http://127.0.0.1:5000/download';

@Injectable({
  providedIn: 'root',
})
export class DownloadFileService {
  constructor(private httpClient: HttpClient) {}

  downloadFile(data: any) {
    const REQUEST_PARAMS = new HttpParams().set('filename', data.fileName);
    return this.httpClient.get(PYTHON_API_DOWNLOAD_FILE, {
      params: REQUEST_PARAMS,
      responseType: 'arraybuffer',
    });
  }
}
