import { Component, OnInit } from '@angular/core';
import { Stream } from '../streams/stream_class';
import { DatafetchService } from '../../services/datafetch.service';
import { Subscription } from 'rxjs';


@Component({
  selector: 'app-streams',
  templateUrl: './streams.component.html',
  styleUrls: ['./streams.component.css']
})
export class StreamsComponent implements OnInit {
  streamsSubs: Subscription;
	streams: Stream[];

  constructor(private dataFetch: DatafetchService) {
    
    
  }

  getStreams() {
    this.streamsSubs = this.dataFetch
    .getStreams()
    .subscribe((streams) =>{
      this.streams = streams as any;
      console.log(this.streams)
    });
    
  };


  ngOnInit() {
    this.getStreams();
  }

}
