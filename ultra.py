#!/usr/bin/python3
# File name   : Ultrasonic.py
# Description : Detection distance and tracking with ultrasonic
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2019/02/23
import RPi.GPIO as GPIO
import time
import move


Tr = 11
Ec = 8

def checkdist():       #Reading distance
    Tr = 11
    Ec = 8
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)
    GPIO.output(Tr, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)
    while not GPIO.input(Ec):
        #print('check-point 1 executed....')
        pass
    print('Moving to Check 2....')
    t1 = time.time()
    while GPIO.input(Ec):
        print('check-point 2 executed....', t1, end=' ')
        pass
    print('Proceeding to Calculation....')
    
    t2 = time.time()
    print('check-point 3 executed....', t2)

    y = (t2-t1)*340/2
    return y
    print("distance = ", y)
    
    
