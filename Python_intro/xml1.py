import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



url = input('Enter_')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('.//count')
sm = 0
for result in results:
    sm = sm+int(result.text)
    #print (result.text)
print (sm)
