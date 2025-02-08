import requests
import json

url = "https://music.youtube.com/youtubei/v1/search"

# Definir o payload (corpo da requisição)
payload = {
    "query": "Bohemian Rhapsody",
    "params": "EgWKAQIIAWoKEAoQCRADEAQQBQ==",
    "context": {
        "client": {
            "clientName": "WEB_REMIX",
            "clientVersion": "1.20240201.01.00"
        }
    }
}

# Definir os headers
headers = {
    "Content-Type": "application/json",
    "Origin": "https://music.youtube.com",
    "Referer": "https://music.youtube.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Fazer a requisição POST
response = requests.post(url, headers=headers, json=payload)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2, ensure_ascii=False))  # Formatar a resposta para melhor visualização
else:
    print(f"Erro {response.status_code}: {response.text}")
