import time
from threading import Timer
#import RPi.GPIO as GPIO
import liveapi
import config as cf
from marshmallow import Schema, fields

# ************************ CLASSES ************************* #

# Time measurement class
class TimeMeasure():
    start_time = 0
    end_time = 0

    def __init__(self):
        self.start_time = time.time()
        self.end_time = time.time()

    def start_measure(self):
        self.start_time = time.time()

    def end_measure(self):
        self.end_time = time.time() - self.start_time

    def print_measure(self, msg = "Time measured: "):
        print(msg + str(self.end_time))


# GPI to Stream class with more information
class GpiStream:
    gpi = 0
    stream_id = '0'
    in_cue = False
    channel_locked = False
    
    def __init__(self, id, gpi):
        self.gpi = gpi
        self.stream_id = id
        self.in_cue = False
        self.channel_locked = False
        
    def __str__(self):
        return "GPI: {} str_id: {} in_cue: {}".format(self.gpi_input, self.stream_id, self.in_cue)
        
    def update_info(self, stream):
        self.in_cue = stream.in_cue
        
    def start_cue(self, elemental_ip = cf.elemental_ip):
        if self.channel_locked is not True:
            response = liveapi.cue_command(elemental_ip, self.stream_id, 'start_cue')
            self.in_cue = True
            self.lock_channel(cf.lock_interval)
            print("3. Starting cue")
            return response
        else:
            print("Channel is locked")
            return "Channel is locked"
        
    def stop_cue(self, elemental_ip = cf.elemental_ip):
        if self.channel_locked is not True:
            response = liveapi.cue_command(elemental_ip, self.stream_id, 'stop_cue')
            self.in_cue = False
            print("3. Stopping cue")
            return response
        else:
            print("Channel is locked")
            return "Channel is locked"

    def lock_channel(self, lock_interval = cf.lock_interval):
        self.channel_locked = True
        unlock_timer = Timer(lock_interval, self.unlock_channnel)
        unlock_timer.start()

    def unlock_channnel(self):
        self.channel_locked = False

#JSON Schema for the GpiStream Class
class StreamSchema(Schema):
    gpi = fields.Number()
    stream_id = fields.Number()
    in_cue = fields.Boolean()
    locked = fields.Boolean()

# ************************ SETUP ****************************** #

reaction_time = TimeMeasure()
# Make a new dict with GPIs as Keys and GpiStreams as values
gpi_stream_dict = {}
for gpi, id in cf.gpi2stream.items():
    gpi_stream_dict[gpi] = GpiStream(id, gpi)


# Setup GPIO inputs/outputs
    #Use Board pin numbering - etc. (12) in pinout command
#GPIO.setmode(GPIO.BCM)
    #Setup GPIOs as inputs with PULL-UP
for GPI in list(cf.gpi2stream):
    pass
    #GPIO.setup( GPI, GPIO.IN, pull_up_down=GPIO.PUD_UP )

# ******* Define callbacks ******* #

# Start cue on Falling edge and Stop Cue on Rising edge
def start_stop_avail(gpi):
    reaction_time.start_measure()

    edge = GPIO.input(gpi)
    stream = gpi_stream_dict[gpi]       # Make a copy of the dict object, for better perfomance
    print("1. {} Event detcted".format(edge))
    print("2. Stream is in cue: {}".format(stream.in_cue))
    
    # Rising edge detected and Stream is in Cue => Stop cue
    if edge and stream.in_cue:        
        stream.stop_cue()

    # Falling edge detected and Stream is NOT in Cue => Start cue
    elif not edge and not stream.in_cue:
        stream.start_cue()
     
    reaction_time.end_measure()
    reaction_time.print_measure()
    gpi_stream_dict[gpi].update_info(stream)    # Update the actual object in the stream dict  

# Tie callbacks to events
for GPI in list(cf.gpi2stream):
    pass
    #GPIO.add_event_detect( GPI, GPIO.BOTH, callback = start_stop_avail, bouncetime = cf.wait_time*1000)
    #GPIO.add_event_detect( GPI, GPIO.BOTH, callback = start_stop_avail, bouncetime = 200)