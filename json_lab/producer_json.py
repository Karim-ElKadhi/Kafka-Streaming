<<<<<<< HEAD
#write your json producer code here
=======
from kafka import KafkaProducer
import csv
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'topic_csv'
json_file = 'transactions.json'


with open(json_file, 'r', newline='', encoding='utf-8') as file:
    data = json.load(file) 

    for record in data:
        producer.send(topic_name, value=record)
        print(f"Message envoyé : {record}")
        time.sleep(1)

producer.flush()
producer.close()
>>>>>>> b0c7375 (Initial commit)
