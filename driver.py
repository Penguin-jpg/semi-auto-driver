import RPi.GPIO as GPIO
import time

class Driver:
    def __init__(self, B1=33, A1=35, B2=32, A2=36):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(B1, GPIO.OUT)
        GPIO.setup(A1, GPIO.OUT)
        GPIO.setup(B2, GPIO.OUT)
        GPIO.setup(A2, GPIO.OUT)

        # right wheel
        self.B1 = B1
        self.A1 = A1
        # left wheel
        self.B2 = B2
        self.A2 = A2

    # B HIGH, A LOW -> clockwise
    # B LOW, A HIGH -> counter-clockwise
    def forward(self):
        print("forward")
        GPIO.output(self.B1, GPIO.HIGH)
        GPIO.output(self.A1, GPIO.LOW)
        GPIO.output(self.B2, GPIO.HIGH)
        GPIO.output(self.A2, GPIO.LOW)
    
    def stop(self):
        GPIO.output(self.B1, GPIO.LOW)
        GPIO.output(self.A1, GPIO.LOW)
        GPIO.output(self.B2, GPIO.LOW)  
        GPIO.output(self.A2, GPIO.LOW)

    def back(self):
        print("back")
        GPIO.output(self.B1, GPIO.LOW)
        GPIO.output(self.A1, GPIO.HIGH)
        GPIO.output(self.B2, GPIO.LOW)
        GPIO.output(self.A2, GPIO.HIGH)

    def left(self):
        print("left")
        GPIO.output(self.B1, GPIO.HIGH)
        GPIO.output(self.A1, GPIO.LOW)
        GPIO.output(self.B2, GPIO.LOW)
        GPIO.output(self.A2, GPIO.LOW)
    

    def right(self):
        print("right")
        GPIO.output(self.B1, GPIO.LOW)
        GPIO.output(self.A1, GPIO.LOW)
        GPIO.output(self.B2, GPIO.HIGH)
        GPIO.output(self.A2, GPIO.LOW)

    def clear(self):
        GPIO.cleanup()
