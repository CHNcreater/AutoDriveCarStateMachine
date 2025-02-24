import sys
sys.path.append("..")
from communication.mqtt_client import MqttClient

class Command:
    def __init__(self, ip_addr):
        self.action = ""
        self.degress = 0
        self.mqtt = MqttClient(ip_addr)

    def execute(self):
        pass