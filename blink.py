#!/usr/bin/env python3
# File name   : blink.py
# Description : Blink and confirm inputs
# Product     : smilebot  
# E-mail      : winicon@live.com
# Author      : Semiu ADEBAYO
# Date        : 2024/08/15
import time
import RPi.GPIO as GPIO

# Change the Pin to the intended pin Number
LED_Pin = 23


# Set up GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Pin, GPIO.OUT)



#GPIO.output(outputLED, GPIO.HIGH)


try:
    while True:

        GPIO.output(LED_Pin, GPIO.HIGH)
        print('LED ON.....RESTARTING....')
        time.sleep(2)

        GPIO.output(LED_Pin, GPIO.LOW)
        print('LED OFF.....RESTARTING....')
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on program exi