
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL:" )
count =    int(input("Enter count:" ))
position =  int(input("Enter position:" ))


def reptation(url_input):
    html = urllib.request.urlopen(url_input, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    counter = 1
    for tag in tags:
        url_f = tag.get('href', None)
        if counter == position:
            break
        counter = counter + 1
    return url_f

for i in range(count):
    url = reptation(url)
    print(url)
