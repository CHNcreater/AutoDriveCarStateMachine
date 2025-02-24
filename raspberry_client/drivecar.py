import RPi.GPIO as GPIO
from models import Wheel
import json

class Drive:
    def __init__(self):
        self.wheel = Wheel()
        self.wheel.start()
    
    def parse_message(self, message):
        data = json.loads(message)
        action, degree = data["action"], data["degree"]
        return action, degree

    def execute(self, action, degree):
        if action == 'left':
            self.turn_left(degree)
        elif action == 'right':
            self.turn_right(degree)
        elif action == 'forward':
            self.move_forward()
        elif action == 'back':
            self.turn_back()
    
    def turn_left(self, degree):
        self.wheel.turn_left(degree)
    
    def turn_right(self, degree):
        self.wheel.turn_right(degree)
    
    def turn_back(self, degree: int = 360):
        self.wheel.turn_left(degree)
    
    def move_forward(self):
        self.wheel.go_straight()