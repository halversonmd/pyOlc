import os
import json

IM_FOLDER = os.listdir('/home/ubuntu/olc_api/contacts')

for file in IM_FOLDER:
    path = os.path.join('/home/ubuntu/olc_api/contacts/' + file)
    with open(path, 'r') as f:
        data = json.loads(f.read())
        print('path', path)
        print('data', json.dumps(data, indent=2))