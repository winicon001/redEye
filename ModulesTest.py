import encoders
import move
import time
import RPi.GPIO as GPIO
import ultra

while True:
    move.setup()
    #move.motor_left(1, 0, 90)
    #move.move(100, 1, "right")
    #encoders.wheelEncodersReading()

    ultra.checkdist()
