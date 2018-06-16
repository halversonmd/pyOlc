import os
import json
import slk
from datetime import date, datetime


CONTACT_FOLDER = os.listdir('/home/ubuntu/olc_api/contacts')


with open('history/times_sent.json', 'r') as f:
    files_sent = json.loads(f.read())
for file in CONTACT_FOLDER:
    if file not in files_sent:
        path = os.path.join('/home/ubuntu/olc_api/contacts/' + file)
        timestamp = file.split('.')[0]
        time_str = datetime.fromtimestamp(float(timestamp)/1000.)
        time_str = date.strftime(time_str, "%m/%d/%Y %I:%M %p")
        with open(path, 'r') as f:
            data = json.loads(f.read())
            data['timestamp'] = time_str
            txt = '```' + json.dumps(data, indent=2) + '```'
            print('path', path)
            print('txt', txt)

        
        web_hook = 'https://hooks.slack.com/services/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'
        slack = slk.OlcSlack(web_hook)
        r = slack.send(txt)
        files_sent.append(file)
        print('added: ', file)
with open('history/times_sent.json', 'w') as f:
    f.write(json.dumps(files_sent))


