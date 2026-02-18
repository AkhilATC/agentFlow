import requests

resp = requests.post(
    "http://localhost:8000/chat",
    json={"query": "Hello, who are you?"}
)

print(resp.json())
