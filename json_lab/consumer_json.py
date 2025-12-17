<<<<<<< HEAD
# Write your json consumer code here
=======
from kafka import KafkaConsumer
import json
from collections import defaultdict
consumer = KafkaConsumer(
    'topic_csv',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)
user_totals = defaultdict(float)

for message in consumer:
    try:
        data = json.loads(message.value.decode('utf-8'))

        user_id = data['user_id']
        amount = float(data['amount'])

        user_totals[user_id] += amount

        print(f"user_id={user_id} | montant total={user_totals[user_id]:.2f}")

    except Exception as e:
        print("Message ignoré :", message.value)
>>>>>>> b0c7375 (Initial commit)
