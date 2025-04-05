import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.kafka_utils import create_producer
import time
import requests
import builtins  # pour éviter le conflit avec round() de PySpark
from dotenv import load_dotenv

# charge les variables du fichier .env
load_dotenv()  

# API Alpha Vantage
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
#"cvoqc99r01qihjtqb380cvoqc99r01qihjtqb38g"  # Remplace par ta vraie clé
FINNHUB_URL = "https://finnhub.io/api/v1/quote"

# Initialisation du Kafka Producer
producer = create_producer()

# Liste des actions à suivre
stocks = ['AAPL', 'MSFT', 'GOOGL']

while True:
    for symbol in stocks:
        try:
            params = {
                "symbol": symbol,
                "token": FINNHUB_API_KEY
            }
            response = requests.get(FINNHUB_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                message = {
                    "symbol": symbol,
                    "price": builtins.round(data["c"], 2),      # prix actuel
                    "high": builtins.round(data["h"], 2),       # plus haut du jour
                    "low": builtins.round(data["l"], 2),        # plus bas du jour
                    "open": builtins.round(data["o"], 2),       # ouverture
                    "previous_close": builtins.round(data["pc"], 2),
                    "timestamp": data["t"]
                }
                producer.send("stock_topic", value=message)
                print(f"📈 Stock envoyé : {message}")
            else:
                print(f"❌ Erreur {symbol} : {response.status_code}")
        except Exception as e:
            print(f"⚠️ Exception pour {symbol} : {e}")
        time.sleep(15)  # pour rester bien en dessous de 30 req/s