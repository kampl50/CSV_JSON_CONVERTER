export interface ConvertRequest {
  file: File;
  settings: ConvertSettings;
}

export interface ConvertSettings {
  from: string;
  to: string;
}
