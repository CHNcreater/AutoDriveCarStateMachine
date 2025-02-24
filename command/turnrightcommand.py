from command.command import Command
import json

class TurnRightCommand(Command):
    def __init__(self, ip_addr):
        super().__init__(ip_addr=ip_addr)

    def execute(self):
        data = {
            "action" : "right",
            "degree" : 0
        }
        self.mqtt.connect()
        self.mqtt.publish(json.dumps(data))