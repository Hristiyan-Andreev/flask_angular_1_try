import sys
import liveapi
import time


from flask import Flask, jsonify
from flask_cors import CORS
from helpers import TimeMeasure, GpiStream, StreamSchema, gpi_stream_dict

# sys.path.append('/home/pi/config') #Only for Raspberry
import config as cf

# Configure the web app (needed only for autorestar)
app = Flask(__name__)
app.config.from_object(cf.FlaskConfig)
CORS(app)



@app.route('/', methods = ['GET'])
def index():
    return "Working"

@app.route('/list_inputs', methods = ['GET'])
def list_inputs():
    schema = StreamSchema(many = True)
    inputs = []
    for gpi, input in gpi_stream_dict.items():
        inputs.append(gpi_stream_dict[gpi].__dict__)
    return jsonify(inputs)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')