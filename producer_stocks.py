from kafka import KafkaProducer
import json
import time
import requests
import builtins  # pour éviter le conflit avec round() de PySpark

# API Alpha Vantage
ALPHA_KEY = "VSH26KK724URKQER"  # Remplace par ta vraie clé
ALPHA_URL = "https://www.alphavantage.co/query"

# Initialisation Kafka
producer = KafkaProducer(
    bootstrap_servers=['kafka:29092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Liste des actions à suivre
stocks = ['AAPL', 'MSFT', 'GOOGL']

# Boucle d’envoi vers Kafka
while True:
    for symbol in stocks:
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": ALPHA_KEY
        }
        response = requests.get(ALPHA_URL, params=params)
        if response.status_code == 200:
            try:
                data = response.json()["Global Quote"]
                message = {
                    "symbol": symbol,
                    "price": builtins.round(float(data["05. price"]), 2),
                    "volume": int(float(data["06. volume"])),
                    "timestamp": time.time()
                }
                producer.send("stock_topic", value=message)
                print(f"📈 Action envoyée : {message}")
            except KeyError:
                print(f"Aucune donnée pour {symbol}")
        else:
            print(f"Erreur API Alpha Vantage : {response.status_code}")
        time.sleep(15)  # Respecter les limites d’Alpha Vantage