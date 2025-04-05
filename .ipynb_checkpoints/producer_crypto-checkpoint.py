from kafka import KafkaProducer
import json
import time
import requests
import builtins  # pour éviter le conflit avec round() de PySpark

# Initialisation du Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['kafka:29092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

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