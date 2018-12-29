import { Component, OnInit } from '@angular/core';
import { Stream } from '../streams/stream_class';
import { DatafetchService } from '../../services/datafetch.service';


@Component({
  selector: 'app-streams',
  templateUrl: './streams.component.html',
  styleUrls: ['./streams.component.css']
})
export class StreamsComponent implements OnInit {
	stream1: Stream = {
		gpi: 16,
		stream_id: 5,
		in_cue: false,
    channel_locked: false,
	};

  constructor(private dataFetch: DatafetchService) {
    this.dataFetch.getStreams();
    
  }

  ngOnInit() {

  }

}
