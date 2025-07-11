"""Send SMS using a simple API from SMS CHEF."""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_secret = os.getenv("SMS_API_KEY")
device_id = os.getenv("DEVICE_ID")
phone = '+254712345678'  # Replace with the actual phone number
message = 'Hello from SMS Chef!'

data = {
  "secret": api_secret,
  "mode": "devices",
  "sim": 1,
  "priority": 1,
  "device": device_id,
  "phone": phone,
  "message": message
}

url = "https://www.cloud.smschef.com/api/send/sms"
r = requests.post(url, data=data, timeout=30)

result = r.json()

print(result)
