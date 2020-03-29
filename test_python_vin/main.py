'''
Created on 27 mar 2020

@author: maxx
'''

import urllib
import ujson
from flask import Flask, jsonify, abort
import socket
import os

app = Flask(__name__)

#URL configuration of the main server. Can be configured by Docker ENV
URL_main_service = os.environ.get('TEST_SERVER_URL', 'https://s3-eu-west-1.amazonaws.com/coding-challenge.carfax.eu/')
#need to think about the need for this setting
SERVER_PORT = os.environ.get('SERVER_PORT', 5000)

#This is needed to return the JSON in the error message.
@app.errorhandler(500)
def error500(json1):
    return jsonify(json1.description), 500

#main service implementation
@app.route("/get_info_by_vin/<VIN>", methods=['GET'])
def get_info_by_vin(VIN):
    try:
        #get data from the main server
        res = urllib.request.urlopen(URL_main_service + VIN , timeout=10)
        data_str = res.read()
    except (urllib.error.HTTPError, urllib.error.URLError) as err:
        abort(500, {"error": "Data not retrieved from URL: {}{}".format(URL_main_service, VIN), "internal_error": str(err), "code": 2})
    except socket.timeout as err:
        abort(500, {"error": "Timeout while retrieve data", "internal_error": str(err), "code": 3})
    except Exception as err:
        abort(500, {"error": "Unknown error while JSON-decode", "internal_error": str(err), "code": 1})
        
    try:
        #decode object from JSON from the main server
        data = ujson.decode(data_str)
    except ValueError as err :
        abort(500, {"error": "Wrong JSON Format from the main service", "internal_error": str(err), "code": 4})
    except Exception as err:
        abort(500, {"error": "Unknown error while JSON-decode", "internal_error": str(err), "code": 1})

    try:
        # Odometer Rollback searching
        if len(data["records"]) < 2:
            return jsonify(data)
        data["records"].sort(key=lambda k:k["date"])
        prev_odo = data["records"][0]["odometer_reading"]
        for val in data["records"]:
            if val["odometer_reading"] < prev_odo:
                val["odometer_rollback"] = True
            prev_odo = val["odometer_reading"]
    except KeyError as err :
        abort(500, {"error": "Wrong JSON Schema from the main service", "internal_error": str(err), "code": 5})
    except Exception as err:
        abort(500, {"error": "Unknown error while rollback search", "internal_error": str(err), "code": 1})
            
    #return data as json
    return jsonify(data)


if __name__ == "__main__":
    # running when standalone app
    app.run(host='0.0.0.0', port=SERVER_PORT)
