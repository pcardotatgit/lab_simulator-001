'''
     for testing sending message Thru SecureX Webhook to webex team room with bot token
    v20221211
'''
import requests
from crayons import *
import config as conf

SecureX_Webhook_url=conf.SecureX_Webhook_url
webex_room_id=conf.webex_room_id
webex_bot_token=conf.webex_bot_token

def send_webhook(ip):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    body_message={'message':'Hello Message sent in the body'}

    body_message={
        "list_of_ips": [ip],
        "roomId":webex_room_id,
        "webex_bot_token":webex_bot_token
    }
    print()
    print(cyan(f'SecureX_Webhook_url : {SecureX_Webhook_url}',bold=True))
    print()
    try:
        print(cyan(f"Trigger SecureX webhook for ip : {ip}",bold=True))
        response = requests.post(SecureX_Webhook_url, headers=headers,data=body_message)
        print(response)
        if response.status_code==202:
            print(green("Webhook Succesfuly sent to SecureX {FLAG:your_are_on_the_road}",bold=True))
            return 1 
        elif response.status_code==401:
            print(red("Error with SecureX webhook probable Bad webhook URL",bold=True))
            return 1             
        else:
            print(red("Webhook Not sent : Unkown Error ( token is ok )",bold=True))
            return 0           
    except:
        response.raise_for_status()
        print(red("Webhook SecureX failed",bold=True))
        return 0

if __name__=="__main__":
    send_webhook("20.20.20.20")