import requests
import datetime

url = "https://discord.com/api/webhooks/1183725396257144902/khDsd4n9m5Exg53ODdAefR88xN1Mq8UEU_cUYcsx7Rpd05tAGqrpXk7rfx9yulqKqBQ-"

def SendMsg(msg:str):

    data = {
        'content' : msg,
        'username': 'DER-L.O.G.'
    }

    r = requests.post(url, json=data)

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        timestamp = datetime.datetime.now()
        print(f'Payload delivered with code {r.status_code} at {timestamp}')