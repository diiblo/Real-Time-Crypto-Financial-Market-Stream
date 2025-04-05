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
    CREATE TABLE IF NOT EXISTS crypto_data (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(10),
        price FLOAT,
        timestamp TIMESTAMPTZ
    );
""")
conn.commit()

# Consommation depuis Kafka
consumer = KafkaConsumer(
    'crypto_topic',
    bootstrap_servers=['kafka:29092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    data = message.value
    print(f"💰 Crypto reçue : {data}")

    cursor.execute("""
        INSERT INTO crypto_data (symbol, price, timestamp)
        VALUES (%s, %s, to_timestamp(%s))
    """, (data["symbol"], data["price"], data["timestamp"]))
    conn.commit()