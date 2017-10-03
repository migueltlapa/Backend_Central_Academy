import urllib.request
import urllib.parse
import re
import json

url='http://centraal.academy'
resp= urllib.request.urlopen(url)
data= resp.read()


result = re.findall(r'<p><(.*?)</p>',str(data))
for item in result[0:6]:
    print("<"+item)


