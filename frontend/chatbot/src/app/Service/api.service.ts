import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  endPoint: string;


  constructor(private http: HttpClient) {
    this.endPoint = "./ask";
   }

   chat(message: string): Observable<any>{
      let payload = {request: message};
      return this.http.post(this.endPoint,payload);
   }

}
