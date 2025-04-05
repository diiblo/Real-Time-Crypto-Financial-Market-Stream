# kafka_utils.py
import json
from kafka import KafkaProducer

def create_producer():
    return KafkaProducer(
        bootstrap_servers=['kafka:29092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )