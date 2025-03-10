import RPi.GPIO as GPIO
import time
# Set Mode
GPIO.setmode(GPIO.BCM)

# Set the Pin input/Output
#A
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.output(17,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
GPIO.output(27,GPIO.LOW)

#B
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

GPIO.output(13,GPIO.HIGH)
GPIO.output(19,GPIO.HIGH)
GPIO.output(26,GPIO.LOW)
#C
GPIO.setup(21,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

GPIO.output(21,GPIO.HIGH)
GPIO.output(20,GPIO.HIGH)
GPIO.output(16,GPIO.LOW)
#D
GPIO.setup(12,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.output(12,GPIO.HIGH)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.HIGH)

# Set  the Initial Duty cycle - 100
a = GPIO.PWM(17,100)
b = GPIO.PWM(13,100)
c = GPIO.PWM(21,100)
d = GPIO.PWM(12,100)

a.start(0)
b.start(0)
c.start(0)
d.start(0)
# Change the Initial Duty cycle from 100 to 10
while True:
    #a.ChangeDutyCycle(15)
    #b.ChangeDutyCycle(15)
    #c.ChangeDutyCycle(15)
    d.ChangeDutyCycle(15)



