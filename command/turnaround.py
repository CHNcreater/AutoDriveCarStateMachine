from command.command import Command
import json

class TurnAroundCommand(Command):
    def __init__(self, ip_addr):
        super().__init__(ip_addr=ip_addr)

    def execute(self):
        data = {
            "action" : "back",
            "degree" : 360
        }
        self.mqtt.connect()
        self.mqtt.publish(json.dumps(data))