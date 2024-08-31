# File name   : encoders.py
# Description : Python Wheel Encoder code for LM393 H2010
# Product     : smilebot  
# E-mail      : winicon@live.com
# Author      : Semiu ADEBAYO
# Date        : 2024/08/15
# credit      : SciJoy @ https://www.youtube.com/watch?v=cLtMcqRetO0&t=101s

import RPi.GPIO as GPIO
import time
#from adafruit_Motorkit import Motorkit

# Encoders Pins Declaration
encoder1 = 15
encoder2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(encoder1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(encoder2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


Encoder1StateLast = GPIO.input(encoder1)
Encoder1rotationCount = 0
Encoder1StateCount = 0
Encoder1StateCountTotal = 0

Encoder2StateLast = GPIO.input(encoder2)
Encoder2rotationCount = 0
Encoder2StateCount = 0
Encoder2StateCountTotal = 0

# Right Wheel Encoder
def wheelEncodersReading():

    Encoder1StateLast = GPIO.input(encoder1)
    Encoder1rotationCount = 0
    Encoder1StateCount = 0
    Encoder1StateCountTotal = 0

    Encoder2StateLast = GPIO.input(encoder2)
    Encoder2rotationCount = 0
    Encoder2StateCount = 0
    Encoder2StateCountTotal = 0

    # Right Wheel Calculation
    wheelCircumference = 204 # Wheel Circumference in mm
    Encoder1StatesPerEncoder1rotation = 40 #Encoder Count Per Wheel Encoder1rotation
    Encoder1distancePerStep = wheelCircumference/Encoder1StatesPerEncoder1rotation # Calculating the Encoder1distance travelled per wheel encoder tick

    # Left Wheel Calculation
    wheelCircumference = 207 # Wheel Circumference in mm
    Encoder2StatesPerEncoder2rotation = 40 #Encoder Count Per Wheel Encoder2rotation
    Encoder2distancePerStep = wheelCircumference/Encoder2StatesPerEncoder2rotation # Calculating the Encoder2distance travelled per wheel encoder tick

    while True:

        #GPIO.output(outputLED, GPIO.HIGH)
        Encoder1StateCurrent = GPIO.input(encoder1)
        if Encoder1StateCurrent != Encoder1StateLast: # If the read value is different from the previous
            Encoder1StateLast = Encoder1StateCurrent # Increment the count
            Encoder1StateCount +=1
            Encoder1StateCountTotal +=1
        
        
        if Encoder1StateCount == Encoder1StatesPerEncoder1rotation:
            Encoder1rotationCount +=1
            Encoder1StateCount = 0
        
        Encoder1distance = Encoder1distancePerStep * Encoder1StateCountTotal



         #GPIO.output(outputLED, GPIO.HIGH)
        Encoder2StateCurrent = GPIO.input(encoder2)
        if Encoder2StateCurrent != Encoder2StateLast: # If the read value is different from the previous
            Encoder2StateLast = Encoder2StateCurrent # Increment the count
            Encoder2StateCount +=1
            Encoder2StateCountTotal +=1
            
            
        if Encoder2StateCount == Encoder2StatesPerEncoder2rotation:
            Encoder2rotationCount +=1
            Encoder2StateCount = 0
        
        Encoder2distance = Encoder2distancePerStep * Encoder2StateCountTotal

        print('   Encoder1StateCount =  ', Encoder1StateCount  , end=' ')
        print('   Encoder1StateCountTotal =  ', Encoder1StateCountTotal, end=' ')
        print('   Encoder1distance =  ', Encoder1distance , end= '  ')

        print('   Encoder2StateCount =  ', Encoder2StateCount  , end=' ')
        print('   Encoder2StateCountTotal =  ', Encoder2StateCountTotal, end=' ')
        print('   Encoder2distance =  ', Encoder2distance, 'mm')

    #except KeyboardInterrupt: # If CTRL+C is pressed
       # kit.motor1.throttle = 0
        #GPIO.cleanup() # End the Process
