<<<<<<< HEAD
#Write your csv producer code here
=======
from kafka import KafkaProducer
import csv
import json
import time

# Configuration du producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'topic_csv'
csv_file = 'data/transactions.csv'

with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file) 

    for row in reader:
        producer.send(topic_name, value=row)
        print(f"Message envoyé : {row}")
        time.sleep(1)  

producer.flush()
producer.close()
>>>>>>> b0c7375 (Initial commit)
