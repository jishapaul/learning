import json


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter_')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



uh = urllib.request.urlopen(url, context=ctx)

data = str(uh.read().decode('utf-8'))

info = json.loads(data)
lst =  (info['comments'])
sm = 0
for k in lst:
    sm = sm + (k['count'])


print (sm)
