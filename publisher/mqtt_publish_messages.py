import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import time
import requests
import random
import decimal
import csv

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

# send a message to the raspberry/topic every 1 second, 5 times in a row
for i in range(5):
    # the four parameters are topic, sending content, QoS and whether retaining the message respectively
    with open('dataset.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            t = str(f'{row["Timestamp"]}')
            k = str(f'{row["Value"]}')
            s = str(f'{row["Sensor"]}')
            data = t+","+k+","+s
            client.publish('raspberry/topic', payload=data, qos=0, retain=False)
            print(f"send {data} to raspberry/topic")
            time.sleep(1)

