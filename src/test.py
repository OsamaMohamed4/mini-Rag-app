import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "deepseek-r1:1.5b",
        "messages": [{"role": "user", "content": "What is SQL?"}],
        "options": {"num_predict": 200, "temperature": 0.1}
    }
)

print(response.text)  # بدل response.json()
