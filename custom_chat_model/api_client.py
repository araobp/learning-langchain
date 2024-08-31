import os
import requests

BASE_URL = "https://api.openai.com/v1"

CHAT_API_URL = "/chat/completions"

# OpenAI API key
API_KEY = os.environ["OPENAI_API_KEY"]
ORG_ID = os.environ["OPENAI_ORG_ID"]
PROJECT_ID = os.environ["OPENAI_PROJECT_ID"]

# OpenAI Model
MODEL = "gpt-3.5-turbo"

HEADERS = {    "Authorization": f"Bearer {API_KEY}",
    "OpenAI-Organization": ORG_ID,
    "OpenAI-Project": PROJECT_ID,
    "Content-Type": "application/json",
}

print(HEADERS)

request_msg = {
    "model": MODEL,
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7,
}

url = BASE_URL + CHAT_API_URL
print(url)
resp = requests.post(url, headers=HEADERS, json=request_msg)
print(resp.status_code)
print(resp.reason)
print(resp.content)
