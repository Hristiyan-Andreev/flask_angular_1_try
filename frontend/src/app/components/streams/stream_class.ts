export class Stream {
	public gpi: number;
	public stream_id: number;
	public in_cue: boolean;
	public channel_locked: boolean;

	constructor(gpi:number, stream_id:number, in_cue:boolean, 
		channel_locked:boolean){
			this.gpi = gpi;
			this.stream_id = stream_id;
			this.channel_locked = channel_locked;
			this.in_cue = in_cue;
		}
	
};