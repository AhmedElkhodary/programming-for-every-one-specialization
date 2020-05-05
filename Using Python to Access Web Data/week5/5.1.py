import urllib.request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_483739.xml'
data = urllib.request.urlopen(url).read()



tree = ET.fromstring(data)


counts = tree.findall('.//count')

total = 0
c = 0
for count in counts:
    total += int(count.text)
    c = c + 1
print ('count: ', c)
print ('sum: ', total)
