import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")
    client.subscribe("car/drive")

def on_message(client, userdata, msg, properties=None):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

broker_address = "192.168.43.240"
port = 1883

client.connect(broker_address, port, 60)
client.publish('car/drive', "hello mqtt")
client.disconnect()