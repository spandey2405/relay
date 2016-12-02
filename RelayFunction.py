import RPi.GPIO as GPIO

from conf import *

class RELAY():
    def __init__(self, **kwargs):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        if "ON" in kwargs:
            self.func = 1
        else:
            self.func = 0

        if "PIN" in kwargs:
            if kwargs['PIN'] == "IN1":
                self.pin = IN1
            elif kwargs['PIN'] == "IN2":
                self.pin = IN2
            elif kwargs['PIN'] == "IN3":
                self.pin = IN3
            elif kwargs['PIN'] == "IN4":
                self.pin = IN4
            else:
                self.pin = IN1
        else:
            self.pin = IN1

        GPIO.setup(self.pin, GPIO.OUT)

    @property
    def switch(self):
        GPIO.output(self.pin, self.func)
        print "RELAY SWITCH TO " + str(self.func)
        return True
