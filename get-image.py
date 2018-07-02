import requests
import random
import os
import re

s = requests.session()
s.headers['user-agent'] = 'doggobot/01.1.0'

resp = s.get('https://www.reddit.com/r/rarepuppers/.json')
resp.raise_for_status()
data = resp.json()

images = [
	p['data']
	for p
	in data['data']['children']
	if p['data']['url'].endswith('.jpg')
]

image = random.choice(images)

resp = s.get(image['url'])
resp.raise_for_status()
data = resp.content

filename = re.sub(r'\W+', '-', image['title'].lower()) + '.jpg'
pathname = os.path.join(os.environ.get('VH_OUTPUTS_DIR', '.'), filename)

with open(pathname, 'wb') as outf:
	outf.write(data)
	print(outf.tell())
	print(pathname)
