import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Stream } from '../components/streams/stream_class'
import { Config } from 'protractor';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class DatafetchService {

  constructor(public http: HttpClient) {
    console.log("Data service connected")
   }

   
   getStreams() {
     return this.http
      .get('http://127.0.0.1:5000/list_inputs');
   }
}
