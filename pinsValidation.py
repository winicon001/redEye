#!/usr/bin/env python3
# File name   : blink.py
# Description : Blink and confirm inputs
# Product     : smilebot  
# E-mail      : swinicon@live.com
# Author      : Semiu ADEBAYO
# Date        : 2024/08/15
import time
import RPi.GPIO as GPIO

# Change the Pin to the intended pin Number
#LED_Pin    = 12, 23
#LED_Pin    = 24
#LED_Pin    = 15
outputLED = 23
encoder1 = 1
#encoder2 = 25
count = 0


# Set up GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(outputLED, GPIO.OUT)
GPIO.setup(encoder1, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#GPIO.output(outputLED, GPIO.HIGH)


while True:

    input = GPIO.input(encoder1)

    if input == GPIO.LOW:
        count +=1
        print('LED ON.....RESTARTING....', end=' ')
        print('Count =  ', count)
    else:
        print('LED OFF.....RESTARTING....', end=' ')
        print('Count = ', count)

    
    #GPIO.output(LED_Pin, GPIO.LOW)
    #time.sleep(1)
    #print('LED OFF.....RESTARTING....')
    #print('Pin Number =', LED_Pin)

GPIO.cleanup()