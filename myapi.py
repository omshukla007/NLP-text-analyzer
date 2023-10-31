''' Making API calls and recieving responses '''

import paralleldots as pds
import configparser as cfgp
import requests as req
import json


class MyAPI:

    # Setting up the API Key ...

    def __init__(self):

        cfg = cfgp.ConfigParser()
        cfg.read('settings.cfg')
        self.api_key = cfg.get('PD', 'api_key')

        pds.set_api_key(apikey=self.api_key)

    # Responses for Sentiment Analysis ...

    def sentiment(self, text):
        response = pds.sentiment(text=text)
        return response

    # Responses for Named Entity Recognition ...

    def ner(self, text):
        response = pds.ner(text=text)
        return response

    # Responses for Intent Classification ...

    def intentc(self, text):
        response = req.post("https://apis.paralleldots.com/v4/new/intent",
                            data={"api_key": self.api_key, "text": text})
        return response


if __name__ == "__main__":

    sample = MyAPI()
    text = input("\n Enter the text : ")
    res = sample.intentc(text=text).json()['intent']

    for i, j in res.items():
        if i not in ['marketing', 'feedback']:
            print(f"{i}\t   :\t{j*100}%")
        elif i=='marketing':
            print(f"{i}  :\t{j*100}%")
        elif i=='feedback':
            print(f"{i}   :\t{j*100}%")
