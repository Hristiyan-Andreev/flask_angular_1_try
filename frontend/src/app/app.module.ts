import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { StreamsComponent } from './components/streams/streams.component';
import { DatafetchService } from './services/datafetch.service';

@NgModule({
  declarations: [
    AppComponent,
    StreamsComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [DatafetchService],
  bootstrap: [AppComponent]
})
export class AppModule { }
