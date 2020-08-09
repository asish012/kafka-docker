from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['192.168.0.6:32785'],
    value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(5)
