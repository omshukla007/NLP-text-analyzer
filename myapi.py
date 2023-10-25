''' Making API calls and recieving responses '''

import paralleldots as pds


class MyAPI:

    # Setting up the API Key ...

    def __init__(self):
        pds.set_api_key('x7JLrbFYLd97Sn11LTx4PFyx25pUAGacyk8E5W73SoU')

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


# if __name__ == "__main__":

#     sample = MyAPI()
#     text = input("\n Enter the text : ")
#     res = sample.sentiment(text=text)

#     response = ''
#     for i in res['sentiment']:
#         response += i.title() + ' \t->\t' + \
#             f"{round(res['sentiment'][i]*100,2)} %\n"
