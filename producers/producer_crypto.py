import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.kafka_utils import create_producer
import time
import requests
import builtins  # pour éviter le conflit avec round() de PySpark

# Initialisation du Kafka Producer
producer = create_producer()

cryptos = ['BTC', 'ETH', 'BNB']
API_URL = "https://min-api.cryptocompare.com/data/price"

while True:
    for symbol in cryptos:
        params = {"fsym": symbol, "tsyms": "USD"}
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            price = response.json()["USD"]
            message = {
                "symbol": symbol,
                "price": builtins.round(price, 2),
                "timestamp": time.time()
            }
            producer.send("crypto_topic", value=message)
            print(f"✅ Crypto envoyée : {message}")
        else:
            print(f"❌ Erreur API pour {symbol}")
        time.sleep(3)