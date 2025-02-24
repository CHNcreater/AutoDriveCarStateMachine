from command.command import Command
import json

class TurnLeftCommand(Command):
    def __init__(self, ip_addr):
        super().__init__(ip_addr=ip_addr)

    def execute(self):
        data = {
            "action" : "left",
            "degree" : 0
        }
        self.mqtt.connect()
        self.mqtt.publish(json.dumps(data))