import CHIP_IO.GPIO as GPIO
import time

class Sprinkler(object):
    # Sprinkler Status
    self.on = False

    def __init__(self, name, pin):
        # Name of the sprinkler bank
        self.name = name
        # Sprinkler Pin
        self.pin = pin

    def initializeGPIO(self):
        GPIO.setup(self.pin, GPIO.OUT, initial=1)
        self.stop()

    def start(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.on = True

    def stop(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.on = False

    def isOn(self):
        return self.on
