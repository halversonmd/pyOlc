import requests
import json

class OlcSlack(object):

    def __init__(self, webhook):
        self._webhook = webhook

    def send(self, text):
        dct = {'text':text}
        r=requests.post(self._webhook, data=json.dumps(dct),verify=False,headers={"Content-Type":'application/json'})
        if r.status_code != 200:
            raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (r.status_code, r.text))

        return r
