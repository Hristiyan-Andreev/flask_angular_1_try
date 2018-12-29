import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Config } from 'protractor';

@Injectable({
  providedIn: 'root'
})

export class DatafetchService {

  constructor(public http: HttpClient) {
    console.log("Data service connected")
   }

   getStreams(){
     this.http.get('http://127.0.0.1:5000/list_inputs')
      .subscribe((streams) => {
        console.log(streams);
      });
   }
}
