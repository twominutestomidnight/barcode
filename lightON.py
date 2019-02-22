import time
import requests
from requests.auth import HTTPDigestAuth
from detect_barcode import handle_bar_code

def light():
    url = 'http://192.168.30.165/ISAPI/Streaming/channels/1/picture'
    #url = 'http://192.168.30.50/ISAPI/System/IO/outputs/1/trigger'
    r = requests.get(url, auth=HTTPDigestAuth('', ''),)
    if r.status_code == 200:
        with open("C:\\Users\\User\\PycharmProjects\\newTest\\sample.jpg", 'wb') as f:
            f.write(r.content)
            handle_bar_code("sample.jpg")
            #handle_bar_code("ewq.jpg")
#light()






