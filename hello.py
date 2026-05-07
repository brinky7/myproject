import requests
response = requests.get('https://api.github.com')
print(f"Статус: {response.status_code}")  # 200 = успех