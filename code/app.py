# version 20221211
from flask import Flask, flash, redirect, render_template, request, session, abort, send_file
import os
from create_incident_and_sightings_with_dynamic_data import create_incident_with_sightings
import config as conf
from send_webhook_to_secureX import send_webhook
from crayons import *
from generate_and_save_token import check_secureX
import webbrowser
import threading
import time

host=conf.host
ctr_client_id=conf.ctr_client_id
ctr_client_password=conf.ctr_client_password

hacked=0

def open_browser_tab(host, port):
    url = 'http://%s:%s/' % (host, port)

    def _open_tab(url):
        time.sleep(1.5)
        webbrowser.open_new_tab(url)

    thread = threading.Thread(target=_open_tab, args=(url,))
    thread.daemon = True
    thread.start()
    
def parse_config(text_content):
    text_lines=text_content.split('\n')
    conf_result=['','','','','','']
    for line in text_lines:
        print(green(line,bold=True))
        if 'ctr_client_id' in line:
            conf_result[0]=line.split('=')[1]
            conf_result[0]=conf_result[0].replace('"','')
        elif 'ctr_client_password' in line:
            conf_result[1]=line.split('=')[1]
            conf_result[1]=conf_result[1].replace('"','')  
        elif 'host="https://private.intel.eu.amp.cisco.com"' in line and line[0]!='#':
            conf_result[2]="EU"  
        elif 'host="https://private.intel.amp.cisco.com"' in line and line[0]!='#':
            conf_result[2]="US"  
        elif 'host="https://private.intel.apjc.amp.cisco.com"' in line and line[0]!='#':
            conf_result[2]="APJC"    
        elif 'SecureX_Webhook_url' in line:
            parts=line.split('url="')
            print(yellow(parts))        
            conf_result[3]=parts[1]
            conf_result[3]=conf_result[3].replace('"','')   
        elif 'webex_bot_token' in line:
            conf_result[5]=line.split('=')[1]
            conf_result[5]=conf_result[5].replace('"','') 
            conf_result[5]=conf_result[5].replace("'","")
        elif 'webex_room_id' in line:
            conf_result[4]=line.split('=')[1]
            conf_result[4]=conf_result[4].replace('"','') 
            conf_result[4]=conf_result[4].replace("'","")
    print(red(conf_result))
    return conf_result

    
    
app = Flask(__name__)

@app.route('/config_and_checks')
def config_and_checks(): 
    return render_template('config_and_checks.html')
    
@app.route('/config')
def config(): 
    with open('config.py','r') as file:
        text_content=file.read()
    conf_params=parse_config(text_content)
    print(cyan(conf_params))    
    return render_template('config.html',conf=conf_params)    

@app.route('/update_config',methods=['POST'])
def update_config(): 
    global host    
    global host_for_token
    global ctr_client_id
    global ctr_client_password    
    line_out="""'''
    this script contains global variables used in several scripts
    you can decided to not use this config file in order to not risk to share credentials accidentally with other
    then don't change anything here but store credentials in text file in folder ../keys
'''
    
"""
    ctr_client_id = request.form.get('client_id')
    print(cyan(f"ctr_client_id : {ctr_client_id}",bold=True))
    ctr_client_password = request.form.get('client_password')
    print(cyan(f"ctr_client_password : {ctr_client_password}",bold=True))
    region = request.form.get('region')
    print(cyan(f"region : {region}",bold=True))    
    webhook_url = request.form.get('webhook_url')
    print(cyan(f"webhook_url : {webhook_url}",bold=True))  
    roomID = request.form.get('roomID')
    print(cyan(f"roomID : {roomID}",bold=True))    
    bot_token = request.form.get('bot_token')
    print(cyan(f"bot_token : {bot_token}",bold=True))     
    line_out=line_out+'ctr_client_id="'+ctr_client_id+'"\n'
    line_out=line_out+'ctr_client_password="'+ctr_client_password+'"\n'
    if region=="EU":
        line_out=line_out+'host="https://private.intel.eu.amp.cisco.com"\n'
        line_out=line_out+'host_for_token="https://visibility.eu.amp.cisco.com"\n'
        host="https://private.intel.eu.amp.cisco.com"
        host_for_token="https://visibility.eu.amp.cisco.com"
    elif region=="US":
        line_out=line_out+'host="https://private.intel.amp.cisco.com"\n'
        line_out=line_out+'host_for_token="https://visibility.amp.cisco.com"\n'   
        host="https://private.intel.amp.cisco.com"
        host_for_token="https://visibility.amp.cisco.com"        
    if region=="APJC":
        line_out=line_out+'host="https://private.intel.apjc.amp.cisco.com"\n'
        line_out=line_out+'host_for_token="https://visibility.apjc.amp.cisco.com"\n'   
        host="https://private.intel.apjc.amp.cisco.com"
        host_for_token="https://visibility.apjc.amp.cisco.com"        
    line_out=line_out+'SecureX_Webhook_url="'+webhook_url+'"\n'
    line_out=line_out+'webex_bot_token="'+bot_token+'"\n' 
    line_out=line_out+'webex_room_id="'+roomID+'"\n'  
    line_out=line_out+'lab_date=""\n'        
    with open('config.py','w') as file: 
        file.write(line_out)
    return "<center><h1>CONFIG FILE MODIFIED</h1><form action='check'><input type='submit' value='Check SecureX'/></form></center>"    

@app.route('/clean_config',methods=['GET'])
def clean_config(): 
    global host    
    global host_for_token
    global ctr_client_id
    global ctr_client_password  
    host=""
    host_for_token=""
    ctr_client_id=""
    ctr_client_password=""
    line_out="""'''
    this script contains global variables used in several scripts
    you can decided to not use this config file in order to not risk to share credentials accidentally with other
    then don't change anything here but store credentials in text file in folder ../keys
'''
    
"""
    line_out=line_out+'ctr_client_id=""\n'
    line_out=line_out+'ctr_client_password=""\n'
    line_out=line_out+'host="https://private.intel.eu.amp.cisco.com"\n'
    line_out=line_out+'host_for_token="https://visibility.eu.amp.cisco.com"\n'   
    line_out=line_out+'SecureX_Webhook_url=""\n'
    line_out=line_out+'webex_bot_token=""\n' 
    line_out=line_out+'webex_room_id=""\n'  
    line_out=line_out+'lab_date=""\n'    
    with open('config.py','w') as file: 
        file.write(line_out)
    with open('ctr_token','w') as file: 
        file.write("***")        
    return "<center><h1>CONFIG FILE MODIFIED</h1><form action='check'><input type='submit' value='Check SecureX'/></form></center>"    
    
@app.route('/check')
def check(): 
    result=check_secureX()
    if result==1:
        return "<center><span style='color:green'><h1>GOOD <br>Connexion with Threat Response is OK</h1>( aks for a ctr = OK and read incidents = ok )</span></center>"
        #return "<center><h1>GOOD - Connexion with Threat Response is OK </h1><h2>{FLAG:READY_TO_GO}</h2></center>"
    if result==2:
        return "<center><span style='color:red'><h1>Something went wrong with asking for token <br> check host_for_token and API credentials</h1></span><form action='config'><input type='submit' value='Configuration'/></form></center></center>"        
    else:
        return "<center><span style='color:red'><h1>Something went wrong with asking for token <br> check host_for_token and API credentials</h1></span><form action='config'><input type='submit' value='Configuration'/></form></center></center>"
    
@app.route('/block',methods=['GET'])
def block():
    if request.args['ip']=='91.109.190.8':
        ip_to_block = request.args['ip']+"FLAGYouRockMan"
    else:
        ip_to_block = request.args['ip']
    print(cyan(f"IP to block is : {ip_to_block}",bold=True))    
    if send_webhook(ip_to_block):
        return "<h2>IP address was succesfully sent to SecureX blocking feed Update workflow</h2>"
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
    global hacked
    if hacked==1:
        hacked=2
        return render_template('pwnd-2.html')
    if hacked==2:
        return render_template('portal.html')        
    else:
        return render_template('safe.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404 
    
    
if __name__ == "__main__":
    open_browser_tab("127.0.0.1",4000)
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0', port=4000)