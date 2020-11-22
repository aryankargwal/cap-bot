import requests
import secrets

secret = secrets.token_urlsafe(16)
payload = {'csv_file': secret+'.csv'}

files = {'file': open('me.jpg', 'rb')}

search = {'keywords': ['beard', 'man']}

# r1 = requests.post("http://localhost:5000/session", params=payload)
# print(r1.text)
# r2 = requests.post("http://localhost:5000/upload", files=files)
# print(r2.text)
r3 = requests.post("http://localhost:5000/search")
print(r3.text)