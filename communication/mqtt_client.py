import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker_address, port=1883, client_id=""):
        self.broker_address = broker_address
        self.port = port
        self.client_id = client_id
        self.client = mqtt.Client(client_id)

    def connect(self):
        self.client.connect(self.broker_address, self.port)

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def disconnect(self):
        self.client.disconnect()

# Example usage:
# mqtt_client = MQTTClient("broker.hivemq.com")
# mqtt_client.connect()
# mqtt_client.publish("test/topic", "Hello MQTT")
# mqtt_client.disconnect()