import requests
from requests.auth import HTTPDigestAuth
from lightON import light
import time


url = 'http://192.168.30.165/ISAPI/Event/notification/alertStream'
str2 = "<eventDescription>Motion alarm</eventDescription>"
str4 = "<eventType>videoloss</eventType>"
str1 = "<eventDescription>IO alarm</eventDescription>"
f = open("lllog.log", "w")
#time.sleep(10)
#light()

r = requests.get(url, auth=HTTPDigestAuth('', ''), stream=True)
for line in r.iter_lines():
    #print("typeOf : ", type(line))
    #print(line)
    line = line.decode("utf-8")
    f.write(line + "\n")
    time.sleep(5)
    light()
    if line == str2:
        print("Motion alarm")

    if line == str4:
        print("videoloss")

    if line == str1:
        print("IO alarm")
        time.sleep(5)
        light()

