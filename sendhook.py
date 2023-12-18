import requests
import datetime

class Webhook():

    def __init__(self, name:str="Der-L.O.G.", msg:str="", url:str="https://discord.com/api/webhooks/1183725396257144902/khDsd4n9m5Exg53ODdAefR88xN1Mq8UEU_cUYcsx7Rpd05tAGqrpXk7rfx9yulqKqBQ-"):
        self.name = name
        self.msg = msg
        self.url = url

    def sendMessage(self):
        # save data in a dict
        data = {
        'content' : self.msg,
        'username': f'{self.name}'
        }
        # create request to post with given data
        r = requests.post(self.url, json=data)

        try:
            #
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            # print error if something goes wrong
            print(err)
        else:
            # save current datetime
            timestamp = datetime.datetime.now()
            # print if the request was succesfull http status and current datetime
            print(f'Payload delivered with code {r.status_code} at {timestamp}')