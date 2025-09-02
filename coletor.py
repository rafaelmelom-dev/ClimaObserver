import requests
import json
from pathlib import Path
from datetime import datetime
import os

API_KEY = os.getenv('OPENWEATHER_API_KEY')
if not API_KEY:
    raise ValueError("API Key not found. Please set the OPENWEATHER_API_KEY environment variable.")

UFU_LAT = -18.7235168
UFU_LON = -47.5253142
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={UFU_LAT}&lon={UFU_LON}&appid=c1f4339a42ed25919964e42cc5afc1b2&units=metric"

response = requests.get(URL)
data = response.json()

if (data['cod'] == 200):
    agora = datetime.now()
    pasta_destino = Path(f"data_lake/raw/weather/ufu/{agora.year}/{agora.month:02d}/{agora.day:02d}")
    pasta_destino.mkdir(parents=True, exist_ok=True)

    nome_arquivo = f"{agora.strftime('%Y-%m-%d_%H-%M-%S')}.json"
    caminho_completo = pasta_destino / nome_arquivo

    with open(caminho_completo, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Data saved to: {caminho_completo}")
