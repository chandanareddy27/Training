import requests
import os
from dotenv import load_dotenv
api_key = os.getenv("HF_API_KEY")
if not api_key:
    print("API key not found")
headers={"authorization":f"bearer {api_key}}
url="https://hf.co/pricing"
payload='{"inputs":"write a quotation for success"}'
data = requests.post(url,headers=headers,json=payload)
result = data.json()
print(result)

