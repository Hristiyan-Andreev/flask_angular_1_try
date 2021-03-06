# Raspberry GPIO dependencies
import time
import RPi.GPIO as GPIO
# Config files
import config as cf
# Elemental Live API commands
import liveapi

# Make a new dict with GPIs as Keys and GpiStreams as values
gpi_stream_dict = {}
for gpi, id in cf.gpi2stream.items():
    gpi_stream_dict[gpi] = GpiStream(id)

reaction_time = TimeMeasure() # To measure the reaction time of the calls

# Setup GPIO inputs/outputs
    # Use Board pin numbering - etc. (12) in pinout command
GPIO.setmode(GPIO.BCM)

    # Setup GPIOs as inputs with PULL-UP
for GPI in list(cf.gpi2stream):
    GPIO.setup( GPI, GPIO.IN, pull_up_down=GPIO.PUD_UP )

# Define callbacks

	# Start cue on Falling edge and Stop Cue on Rising edge
def start_stop_avail(gpi):
    edge = GPIO.input(gpi)
    stream = gpi_stream_dict[gpi]           # Make a copy of the dict object, for better perfomance
    print("1. {} Event detcted".format(edge))
    print("2. Stream is in cue: {}".format(stream.in_cue))
    
    # Rising edge detected and Stream is in Cue => Stop cue
    if edge and stream.in_cue:  
        print("3. Stopping cue")
        reaction_time.start_measure()
        #resp = liveapi.cue_command(cf.elemental_ip, cf.gpi2stream[gpi], 'stop_cue') # Stop cue
        stream.stop_cue()
        
        reaction_time.end_measure()
        reaction_time.print_measure()
        
        stream.in_cue = False       # Stream is no longer in cue
        gpi_stream_dict[gpi].update_info(stream)    # Update the actual object in the stream dict       
        time.sleep(cf.wait_time)                    # Sleeps the thread for all GPIO inputs - not good
        
    # Falling edge detected and Stream is NOT in Cue => Start cue
    elif not edge and not stream.in_cue:    
        print("3. Starting cue")
        reaction_time.start_measure()
        #resp = liveapi.cue_command(cf.elemental_ip, cf.gpi2stream[gpi], 'start_cue') # Start cue
        stream.start_cue()
        
        reaction_time.end_measure()
        reaction_time.print_measure()
        
        stream.in_cue = True          # Stream is now in cue
        gpi_stream_dict[gpi].update_info(stream)    # Update the actual object in the stream dict
        time.sleep(cf.wait_time)                    # Sleeps the thread for all GPIO inputs - not good
        

# Tie callbacks to events
for GPI in list(cf.gpi2stream):
    #GPIO.add_event_detect( GPI, GPIO.BOTH, callback = start_stop_avail, bouncetime = cf.wait_time*1000)
    GPIO.add_event_detect( GPI, GPIO.BOTH, callback = start_stop_avail)