
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ' http://py4e-data.dr-chuck.net/comments_483737.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
ismall_list = list()
count = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    small_list = str(tag)
    numbers_in_line = re.findall('[0-9]+',small_list)
    ismall_list.append(int(numbers_in_line[0]))

print('Count ',len(ismall_list))
print(sum(ismall_list))
