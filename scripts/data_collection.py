import requests
import csv
import time

# Lista de URLs da API do Spotify a serem monitoradas
api_endpoints = [
    "https://api.spotify.com/v1/browse/new-releases",
    "https://api.spotify.com/v1/browse/featured-playlists",
    "https://api.spotify.com/v1/search?q=adele&type=track"
]

# Token de acesso à API do Spotify (gerado previamente)
spotify_token = "SEU_TOKEN_DE_ACESSO"

# Headers com o token de autorização
headers = {
    "Authorization": f"Bearer {spotify_token}"
}

# Função para coletar dados das APIs do Spotify
def collect_data(api_endpoints):
    data = []
    for endpoint in api_endpoints:
        start_time = time.time()
        response = requests.get(endpoint, headers=headers)
        end_time = time.time()
        response_time = end_time - start_time
        status_code = response.status_code
        data.append({'API_ENDPOINT': endpoint, 'STATUS_CODE': status_code, 'RESPONSE_TIME': response_time})
    return data

# Função para salvar dados em um arquivo CSV
def save_to_csv(data):
    with open('spotify_api_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['API_ENDPOINT', 'STATUS_CODE', 'RESPONSE_TIME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    api_data = collect_data(api_endpoints)
    save_to_csv(api_data)
