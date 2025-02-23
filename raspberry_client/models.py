import RPi.GPIO as GPIO
import time

class Wheel: 
    def __init__(self):
        self.LEFT_MOTOR_FORWARD_VCC = 20
        self.LEFT_MOTOR_FORWARD_GND = 16
        self.LEFT_MOTOR_FORWARD_PWM = 21
        self.LEFT_MOTOR_BACKWARD_VCC = 23
        self.LEFT_MOTOR_BACKWARD_GND = 24
        self.LEFT_MOTOR_BACKWARD_PWM = 12
        self.RIGHT_MOTOR_FORWARD_VCC = 19
        self.RIGHT_MOTOR_FORWARD_GND = 26
        self.RIGHT_MOTOR_FORWARD_PWM = 13
        self.RIGHT_MOTOR_BACKWARD_VCC = 18
        self.RIGHT_MOTOR_BACKWARD_GND = 27
        self.RIGHT_MOTOR_BACKWARD_PWM = 17
        self.LEFT_FRONT_MOTOR = None
        self.LEFT_BACK_MOTOR = None
        self.RIGHT_FRONT_MOTOR = None
        self.RIGHT_BACK_MOTOR = None
        self.setup()
        self.setup_output()
        self.Initial_DutyCycle()
        self.duty_cycle = 10
        self.frequency = 100

    def setup(self):
        GPIO.setup(self.LEFT_MOTOR_FORWARD_VCC, GPIO.OUT)
        GPIO.setup(self.LEFT_MOTOR_FORWARD_GND, GPIO.OUT)
        GPIO.setup(self.LEFT_MOTOR_FORWARD_PWM, GPIO.OUT)
        GPIO.setup(self.LEFT_MOTOR_BACKWARD_VCC, GPIO.OUT)
        GPIO.setup(self.LEFT_MOTOR_BACKWARD_GND, GPIO.OUT)
        GPIO.setup(self.LEFT_MOTOR_BACKWARD_PWM, GPIO.OUT)
        GPIO.setup(self.RIGHT_MOTOR_FORWARD_VCC, GPIO.OUT)
        GPIO.setup(self.RIGHT_MOTOR_FORWARD_GND, GPIO.OUT)
        GPIO.setup(self.RIGHT_MOTOR_FORWARD_PWM, GPIO.OUT)
        GPIO.setup(self.RIGHT_MOTOR_BACKWARD_VCC, GPIO.OUT)
        GPIO.setup(self.RIGHT_MOTOR_BACKWARD_GND, GPIO.OUT)
        GPIO.setup(self.RIGHT_MOTOR_BACKWARD_PWM, GPIO.OUT)

    def setup_output(self):
        GPIO.output(self.LEFT_MOTOR_FORWARD_VCC, GPIO.LOW)
        GPIO.output(self.LEFT_MOTOR_FORWARD_GND, GPIO.HIGH)
        GPIO.output(self.LEFT_MOTOR_FORWARD_PWM, GPIO.HIGH)
        GPIO.output(self.LEFT_MOTOR_BACKWARD_VCC, GPIO.LOW)
        GPIO.output(self.LEFT_MOTOR_BACKWARD_GND, GPIO.HIGH)
        GPIO.output(self.LEFT_MOTOR_BACKWARD_PWM, GPIO.HIGH)
        GPIO.output(self.RIGHT_MOTOR_FORWARD_VCC, GPIO.LOW)
        GPIO.output(self.RIGHT_MOTOR_FORWARD_GND, GPIO.HIGH)
        GPIO.output(self.RIGHT_MOTOR_FORWARD_PWM, GPIO.HIGH)
        GPIO.output(self.RIGHT_MOTOR_BACKWARD_VCC, GPIO.LOW)
        GPIO.output(self.RIGHT_MOTOR_BACKWARD_GND, GPIO.HIGH)
        GPIO.output(self.RIGHT_MOTOR_BACKWARD_PWM, GPIO.HIGH)

    def Initial_DutyCycle(self):
        self.LEFT_FRONT_MOTOR = GPIO.PWM(self.LEFT_MOTOR_FORWARD_PWM, self.frequency)
        self.LEFT_BACK_MOTOR = GPIO.PWM(self.LEFT_MOTOR_BACKWARD_PWM, self.frequency)
        self.RIGHT_FRONT_MOTOR = GPIO.PWM(self.RIGHT_MOTOR_FORWARD_PWM, self.frequency)
        self.RIGHT_BACK_MOTOR = GPIO.PWM(self.RIGHT_MOTOR_BACKWARD_PWM, self.frequency)

    def start(self):
        self.LEFT_FRONT_MOTOR.start(0)
        self.LEFT_BACK_MOTOR.start(0)
        self.RIGHT_FRONT_MOTOR.start(0)
        self.RIGHT_BACK_MOTOR.start(0)
    
    def stop_move(self):
        self.LEFT_FRONT_MOTOR.ChangeDutyCycle(0)
        self.LEFT_BACK_MOTOR.ChangeDutyCycle(0)
        self.RIGHT_FRONT_MOTOR.ChangeDutyCycle(0)
        self.RIGHT_BACK_MOTOR.ChangeDutyCycle(0)
    
    def move(self, time):
        """move the car, set motor's duty cycle and sleep for a while let car move for a moment

        Args:
            time (int): the second of the car move
        """
        self.LEFT_FRONT_MOTOR.ChangeDutyCycle(self.duty_cycle)
        self.LEFT_BACK_MOTOR.ChangeDutyCycle(self.duty_cycle)
        self.RIGHT_FRONT_MOTOR.ChangeDutyCycle(self.duty_cycle)
        self.RIGHT_BACK_MOTOR.ChangeDutyCycle(self.duty_cycle)
        time.sleep(time)
        self.stop_move()

    def go_straight(self):
        self.move()

    def turn_left(self, degree):
        """turn left, when degree is equal 360, the car will turn around 360 degree

        Args:
            degree (int): the degree of the car turn left
        """
        # left front and back wheel move backward
        GPIO.output(self.LEFT_MOTOR_FORWARD_VCC, GPIO.HIGH)
        GPIO.output(self.LEFT_MOTOR_FORWARD_GND, GPIO.LOW)
        GPIO.output(self.LEFT_MOTOR_BACKWARD_VCC, GPIO.HIGH)
        GPIO.output(self.LEFT_MOTOR_BACKWARD_GND, GPIO.LOW)
        self.move(1)

    def turn_right(self, degree):
        """turn right

        Args:
            degree (int): the degree of the car turn right
        """
        # right front and back wheel move backward
        GPIO.output(self.RIGHT_MOTOR_FORWARD_VCC, GPIO.HIGH)
        GPIO.output(self.RIGHT_MOTOR_FORWARD_GND, GPIO.LOW)
        GPIO.output(self.RIGHT_MOTOR_BACKWARD_VCC, GPIO.HIGH)
        GPIO.output(self.RIGHT_MOTOR_BACKWARD_GND, GPIO.LOW)
        self.move(1)