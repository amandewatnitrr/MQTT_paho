# MQTT
<p align="center">
  <img src="https://github.com/amandewatnitrr/MQTT/blob/main/imgs/IoT.gif" width="30%" height=20%>
</p>
<p align="justify">
MQTT is a lightweight IoT messaging protocol based on the publish/subscribe model, which provides a real-time and reliable messaging service for IoT devices, only using very little code and bandwidth. It is suitable for devices with limited hardware resources and a network environment with limited bandwidth. Therefore, the MQTT protocol is widely used.

This repo mainly presents how to use the paho-MQTT client and execute connection, subscribe, messaging, and other functions between the client and MQTT broker.
</p>

## Project Initialization

This project uses Python 3.6 or 3.7.3 to develop and test. Use the command to confirm the Python version.<br>
```Terminal
python3 --version
```
The Paho Python Client provides a client class with support for both MQTT v3.1 and v3.1.1 on Python 2.7 or 3.x. It also provides some helper functions to make publishing one off messages to an MQTT server very straightforward.

<p align="center">
<img src="https://github.com/amandewatnitrr/MQTT/blob/main/imgs/output-onlinegiftools.gif" width="30%">
</p>

### Installation using pip

```Terminal
pip3 install paho-mqtt
```

or in case you can do it the other way as well.

```Terminal
git clone https://github.com/eclipse/paho.mqtt.python
cd paho.mqtt.python
python setup.py install
```

The accessing information of the broker is as follows:

```python
Broker: broker.emqx.io
TCP Port: 1883
Websocket Port: 8083
```

### MQTT Connect

Function will be called after connecting the client, and we can determine whether the client is connected successfully according to rc in this function. Usually, we will create an MQTT client at the same time and this client will connect to broker.emqx.io.

```Python
# test_connect.py 
import paho.mqtt.client as mqtt 

# The callback function. It will be triggered when trying to connect to the MQTT broker
# client is the client instance connected this time
# userdata is users' information, usually empty. If it is needed, you can set it through user_data_set function.
# flags save the dictionary of broker response flag.
# rc is the response code.
# Generally, we only need to pay attention to whether the response code is 0.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")

client = mqtt.Client() 
client.on_connect = on_connect 
client.connect("broker.emqx.io", 1883, 60) 
client.loop_forever()
```

### Publish Messages

```Python
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
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
```

### Subscribe to Messages


```Subscribe
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
from datetime import datetime
import time
import requests
import random
import decimal
import csv
from time import strptime

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # subscribe, which need to put into on_connect
    # if reconnect after losing the connection with the broker, it will continue to subscribe to the raspberry/topic topic
    client.subscribe("raspberry/topic")

# the callback function, it will be triggered when receiving messages
def on_message(client, userdata, msg):
    data = {msg.payload}
    print(type(f"{msg.topic} {msg.payload}"))
    with open('bmp_180.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally, it will send the will message to other clients
client.will_set('raspberry/status', b'{"status": "Off"}')

# create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
client.connect("broker.emqx.io", 1883, 60)

# set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
client.loop_forever()
```

## Refernces:

1. https://pypi.org/project/paho-mqtt/#single
