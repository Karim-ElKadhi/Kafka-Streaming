<<<<<<< HEAD
# Write your csv consumer code here
=======
from kafka import KafkaConsumer
import json
from collections import defaultdict

consumer = KafkaConsumer(
    'topic_csv',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: x.decode('utf-8')
)
total_amount_by_user = defaultdict(float)

print("Consumer démarré...")

for message in consumer:
    print(f"Message reçu : {message.value}")
>>>>>>> b0c7375 (Initial commit)
