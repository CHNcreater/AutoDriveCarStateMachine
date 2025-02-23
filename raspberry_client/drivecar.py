import RPi.GPIO as GPIO
from models import Wheel

class Drive:
    def __init__(self):
        self.wheel = Wheel()
    
    def parse_message(self, message):
        pass

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