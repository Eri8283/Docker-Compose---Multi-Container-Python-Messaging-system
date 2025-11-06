import requests 
import time

time.sleep(2)

response = requests.get("http://server:5000/")

print(response.text)
