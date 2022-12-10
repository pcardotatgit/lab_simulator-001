'''
    for testing sending message directly to webex team room with bot token
    v20221209
'''
import requests
from crayons import *
import config as conf

DESTINATION_ROOM_ID=conf.webex_room_id
BOT_ACCESS_TOKEN=conf.webex_bot_token

def send_message():
    global BOT_ACCESS_TOKEN
    global DESTINATION_ROOM_ID
    lines=[]
    
    print(cyan(f"BOT_ACCESS_TOKEN = {BOT_ACCESS_TOKEN}",bold=True))
    print(cyan(f"DESTINATION_ROOM_ID = {DESTINATION_ROOM_ID}",bold=True))

    #URL = 'https://api.ciscospark.com/v1/messages'
    URL = 'https://webexapis.com/v1/messages'
    
    MESSAGE_TEXT = 'Hello ! ( test from my python script )'

    headers = {'Authorization': 'Bearer ' + BOT_ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    post_data = {'roomId': DESTINATION_ROOM_ID,
                 'text': MESSAGE_TEXT}
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
    print(yellow(f'Test sending message from bot token to Webex team Room',bold=True))
    print() 
    send_message()