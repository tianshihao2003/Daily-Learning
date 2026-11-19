import requests
import json

url = "https://api.frdic.com/api/open/v1/studylist/category"

payload = json.dumps({
    "language": "en",
    "name": "test"
})
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Authorization': 'NIS j+6KRLJxPHTE7H4+oIb4RsXydyPBuLYLZpnUgDZc2z/LIWs6eCYhdg==',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)