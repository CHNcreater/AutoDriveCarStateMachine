from command.command import Command
import json

class MoveForwardCommand(Command):
    def __init__(self, ip_addr):
        super().__init__(ip_addr=ip_addr)

    def execute(self):
        data = {
            "action" : "forward",
            "degree" : 0
        }
        self.mqtt.connect()
        self.mqtt.publish(json.dumps(data))