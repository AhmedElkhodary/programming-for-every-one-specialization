import urllib.request, urllib.parse, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_483740.json"
data = urllib.request.urlopen(url).read()




info = json.loads(data)


sum = 0
c= 0
for item in info["comments"] :
    c= c + 1
    sum = sum + int(item["count"])

print("Count: ",c)
print("Sum: ",sum)
