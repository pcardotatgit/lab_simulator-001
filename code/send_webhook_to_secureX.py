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

    try:
        print(cyan(f"Trigger SecureX webhook for ip : {ip}",bold=True))
        response = requests.post(SecureX_Webhook_url, headers=headers,data=body_message)
        print(response)
        print(green("Webhook Succesfuly sent to SecureX",bold=True))
        return 1
    except:
        #response.raise_for_status()
        print(red("Webhook SecureX failed",bold=True))
        return 0

