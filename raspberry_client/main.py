import paho.mqtt.client as mqtt
from drivecar import Drive

# Define the MQTT client
client = mqtt.Client()
driver = Drive()

def on_connect(client, userdata, flags, rc):
    print("Connection returned " + str(rc))

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")
    action, degree = driver.parse_message(message.payload.decode())
    driver.execute(action, degree)

# Set the callback function
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("localhost", 1883, 60)

# Subscribe to the topic 'car/drive'
client.subscribe("car/drive")

# Start the MQTT client loop
client.loop_forever()