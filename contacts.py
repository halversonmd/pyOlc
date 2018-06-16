import os
import json
import slk
from datetime import date, datetime


IM_FOLDER = os.listdir('/home/ubuntu/olc_api/contacts')

for file in IM_FOLDER:
    path = os.path.join('/home/ubuntu/olc_api/contacts/' + file)
    timestamp = file.split('.')[0]
    time_str = datetime.fromtimestamp(float(timestamp)/1000.)
    time_str = date.strftime(time_str, "%m/%d/%Y %H:%M %p")
    with open(path, 'r') as f:
        data = json.loads(f.read())
        data['timestamp'] = time_str
        txt = '```' + json.dumps(data, indent=2) + '```'
        print('path', path)
        print('txt', txt)

    
    web_hook = 'https://hooks.slack.com/services/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'
    slack = slk.OlcSlack(web_hook)
    r = slack.send(txt)
    print('slack resp: ', r.text)

