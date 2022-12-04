#from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, send_file
import os
from create_incident_and_sightings_with_dynamic_data import create_incident_with_sightings
import config as conf
from send_webhook_to_secureX import send_webhook
from crayons import *
from generate_and_save_token import check_secureX

host=conf.host
hacked=0

app = Flask(__name__)

@app.route('/check')
def check(): 
    result=check_secureX()
    if result==1:
        return "<center><h1>ALL GOOD</h1></center>"
    if result==2:
        return "<center><h1>Something went wrong with asking for token - check host_for_token and API credentials</h1></center>"        
    else:
        return "<center><h1>Something went wrong with asking for incidents - check host and API credentials</h1></center>"
    
@app.route('/block',methods=['GET'])
def block():
    ip_to_block = request.args['ip']
    print(cyan(f"IP to block is : {ip_to_block}",bold=True))    
    if send_webhook(ip_to_block):
        return "<h1>IP address was succesfully sent to SecureX blocking feed Update workflow</h1>"
    else:
        return "<h1>An Error Occured - IP was NOT sent to Securex blocking feed Update workflow</h1>"
    
@app.route('/a')
def test1():
    global hacked
    hacked=1
    return "<h1>HACKED</h1>"

@app.route('/reset')
def reset():
    global hacked
    hacked=0
    return render_template('safe.html')   
    
@app.route('/hacker')
def hacker():
    return render_template('hacker_console-1.html')
    
@app.route('/cmd')
def cmd():
    global hacked
    hacked=1 
    create_incident_with_sightings(host)
    return render_template('hacker_console-2.html')
    
@app.route('/')
def index():
    if hacked:
        return render_template('pwnd-2.html')
    else:
        return render_template('safe.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404 
    
    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)