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

## Refernces:

1. https://pypi.org/project/paho-mqtt/#single
