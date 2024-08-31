import RPi.GPIO as GPIO
import time

# Set GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the ultrasonic sensor
TRIG_PIN = 11
ECHO_PIN = 8

# Set the trigger and echo pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def get_distance():
    # Send a short pulse to the trigger pin
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Measure the duration for the echo pulse
    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    # Calculate the distance based on the speed of sound (34300 cm/s)
    distance_cm = pulse_duration * 34300 / 2
    return distance_cm

try:
    while True:
        distance = get_distance()
        print(f"Measured Distance: {distance:.1f} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped by user")
finally:
    GPIO.cleanup()