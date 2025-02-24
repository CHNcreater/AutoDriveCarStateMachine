import paho.mqtt.client as mqtt
import sys
sys.path.append("..")
from configuration import Configuration

class MqttClient:
    def __init__(self, broker_address, port=1883):
        self.config = Configuration()
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.borker_address = broker_address
        self.port = port
        
    def on_connect(self, client, userdata, flags, rc, properties=None):
        print(f"Connected with result code {rc}")
        client.subscribe("car/drive")

    def on_message(self, client, userdata, msg, properties=None):
        print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")
        
    def connect(self):
        self.client.connect(self.borker_address, self.port, 60)
        
    def publish(self, message):
        self.client.publish(self.config.get("mqtt", "topic"), message)
        
    def disconnect(self):
        self.client.disconnect()
        
if __name__ == '__main__':
    broker_address = "192.168.43.240"
    mqtt_instance = MqttClient(broker_address=broker_address)
    mqtt_instance.connect()
    mqtt_instance.publish("Hello")
    mqtt_instance.disconnect()