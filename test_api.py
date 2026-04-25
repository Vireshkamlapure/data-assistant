import requests

# The standard OpenAI completion endpoint appended to your base URL
url = "https://llm.optimiq.us/v1/chat/completions"

headers = {
    "Authorization": "Bearer sk-llm-d32a4aa25ce58a759fbecaa2d70f9aa85804ce381e7d30c4",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" # Often helps bypass basic WAF blocks
}

data = {
    "model": "gemma-4",
    "messages": [{"role": "user", "content": "Hello, are you receiving this?"}],
    "temperature": 0
}

print("Sending direct request...")
try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
except Exception as e:
    print(f"Network Error: {e}")