import sys
import liveapi
import time
#import RPi.GPIO as GPIO
from flask import Flask


# sys.path.append('/home/pi/config') #Only for Raspberry
import config as cf

# Configure the web app (needed only for autorestar)
app = Flask(__name__)
app.config.from_object(cf.FlaskConfig)


@app.route('/')
def index():
    return "Working"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')     
