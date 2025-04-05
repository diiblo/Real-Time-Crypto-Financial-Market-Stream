import json
from kafka import KafkaConsumer
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_utils import init_database

# Initialisation BDD
conn, cursor = init_database()

# Créer la table si elle n'existe pas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_data (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    price FLOAT,
    high FLOAT,
    low FLOAT,
    open FLOAT,
    previous_close FLOAT,
    timestamp TIMESTAMPTZ
);
""")
conn.commit()

# Consommation depuis Kafka
consumer = KafkaConsumer(
    'stock_topic',
    bootstrap_servers=['kafka:29092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    data = message.value
    print(f"📈 Stock reçu : {data}")

    cursor.execute("""
    INSERT INTO stock_data (symbol, price, high, low, open, previous_close, timestamp)
    VALUES (%s, %s, %s, %s, %s, %s, to_timestamp(%s))
""", (
    data["symbol"],
    data["price"],
    data["high"],
    data["low"],
    data["open"],
    data["previous_close"],
    data["timestamp"]
))
    conn.commit()
