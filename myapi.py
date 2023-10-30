''' Making API calls and recieving responses '''

import paralleldots as pds
import configparser as cfgp


class MyAPI:

    # Setting up the API Key ...

    def __init__(self):

        cfg = cfgp.ConfigParser()
        cfg.read('settings.cfg')
        api_key = cfg.get('PD', 'api_key')

        pds.set_api_key(apikey=api_key)

    # Responses for Sentiment Analysis ...

    def sentiment(self, text):
        response = pds.sentiment(text=text)
        return response

    # Responses for Named Entity Recognition ...

    def ner(self, text):
        response = pds.ner(text=text)
        return response

    # Responses for Emotion Prediction ...

    def emo(self, text):
        response = pds.emotion(text=text)
        return response


if __name__ == "__main__":

    sample = MyAPI()
    text = input("\n Enter the text : ")
    res = sample.ner(text=text)

    for i in res['entities']:
        print(f"{i['name']} is a {i['category']}.\n")
