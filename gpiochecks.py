import RPi.GPIO as GPIO

# Set the mode to BCM (Broadcom numbering)
GPIO.setmode(GPIO.BCM)

# Iterate through all GPIO pins and print their status
for pin in range(2, 28):  # GPIO pins 2 to 27
    try:
        status = GPIO.gpio_function(pin)
        print(f"GPIO {pin} status: {'Used' if status != GPIO.IN else 'Available'}")
    except:
        print(f"Error reading GPIO {pin}")

# Clean up GPIO configuration
GPIO.cleanup()

