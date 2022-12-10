'''
    Send the Alert Message to the Alert Webex Room
    v20221209
'''
import requests
from crayons import *
import config as conf

DESTINATION_ROOM_ID=conf.webex_room_id
BOT_ACCESS_TOKEN=conf.webex_bot_token

message_out='''
# EndPoint Infection Alert !
---
### An Endpoint Infection had been detected into your company. Immediate action is required !. 
---
### Incident : EndPoint Infection Alert !
---
### Targets :'

- [84.48.25.16 ( block IP into firewalls )](http://localhost:4000/block?ip=84.48.25.16)
- Victim Endpoint ( hostname )
- 57150e86-fcbe-47ff-8bc7-3f297d473b79 ( amp_computer_guid )
- [192.168.0.137 ( block IP into firewalls )](http://localhost:4000/block?ip=192.168.0.137)
### Suspicious / Malicious Observables :\n
- [91.109.190.8 ( block IP into firewalls )](http://localhost:4000/block?ip=192.168.0.137)
- 6f88fb88ffb0f1d5465c2826e5b4f523598b1b8378377c8378ffebc171bad18b ( sha256 )
- [54c0cd40ea153f2b8cdc27c1b1baf96d77505807bda9979f2ba9ccb7ff0db3ed ( sha256 )
'''


def send_message(message):
    global BOT_ACCESS_TOKEN
    global DESTINATION_ROOM_ID
    lines=[]
    
    print(cyan(f"BOT_ACCESS_TOKEN = {BOT_ACCESS_TOKEN}",bold=True))
    print(cyan(f"DESTINATION_ROOM_ID = {DESTINATION_ROOM_ID}",bold=True))

    #URL = 'https://api.ciscospark.com/v1/messages'
    URL = 'https://webexapis.com/v1/messages'


    headers = {'Authorization': 'Bearer ' + BOT_ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    post_data = {'roomId': DESTINATION_ROOM_ID,
                 'markdown': message_out}
    response = requests.post(URL, json=post_data, headers=headers)
    if response.status_code == 200:
        # Great your message was posted!
        #message_id = response.json['id']
        #message_text = response.json['text']
        print(green("New message succesfully sent",bold=True))
        #print(message_text)
        print("====================")
        print(response)
    elif response.status_code == 401:
        print()
        print(red("Error bad authentication token",bold=True))        
    else:
        # Oops something went wrong...  Better do something about it.
        print(red(response.status_code, response.text,bold=True))
        
if __name__ == "__main__":
    print()  
    print(yellow(f'sending alert message from bot token to Webex team Room',bold=True))
    print() 
    send_message(message_out)