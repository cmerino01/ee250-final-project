import base64
import requests

IMGBB_API_KEY = 'd343a394534eeb067389939d0ecb3a53'

def url_call():    
    with open("recent_trend.png", "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": IMGBB_API_KEY,
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)

        response = res
        if response.status_code == 200: # Status: OK
            data = response.json()
            info = data["data"]
            url = info["url_viewer"]
            print(url)