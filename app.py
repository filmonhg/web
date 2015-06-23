from flask import Flask, render_template, redirect, url_for, request, jsonify, json
from cassie_utils import CassieUtilities
import csv
import time
from datetime import datetime, timedelta
import time

app = Flask(__name__)

CUtils = CassieUtilities('52.8.124.34')
@app.route('/index')
def index():
    user = {'nickname': 'Real Time Processing'}  # fake user
    result = CUtils.fetch_daterange(table='outbound_real_count')
    response = []
    for res in result:
        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
    return render_template("realtime.html",
				user=user,
                                posts=response
				); 
@app.route('/realtime')
def realtime():
    user = {'nickname': 'Real Time Processing'}  # fake user
    result = CUtils.fetch_daterange(table='outbound_real_count')
    response = []
    for res in result:
        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]}) 
    return render_template("realtime.html",
				title='Real Time',
				user=user,
				posts=response
				);

@app.route('/batch')
def batch():
    user = {'nickname': 'Batch Processing'}  # fake user
    result = CUtils.fetch_daterange(table='outbound_count')
    print result;
    response = []
    response2 = []
    print "+++++++++++++++"
    j=0
    for res in result:
        i=0
        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
    response2=response
    return render_template("batch.html",
                                title='Real Time',
                                user=user,
                                posts=response,
				posts2=response2
                                );

#@app.route('/batch', method=['POST'])
#def batch_post():
#    city = request.form["City"]
#    state = request.form["State"]
#    result = CUtils.fetch_daterange(table='outbound_count', city, state)
#    response = []
#    print "+++++++++++++++"
#    j=0
#    for res in result:
#        i=0
#        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
#    return render_template("batch.html",
#                                title='Real Time',
#                                user=user,
#                                posts=response
#
#                                );
#
#
@app.route('/map')
def map():
    result = CUtils.fetch_daterange(table='outbound_real_count')
    response = []
    print result
    for res in result:
        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]}) 
    return render_template("test.html",
				title='Map data',
				posts=response
				);
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
