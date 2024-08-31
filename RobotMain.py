import time
import move
import keyPressModule as kp
import RPi.GPIO as GPIO
import ultra

# Key inpt Commands
kp.init()

def main():
# Declaration of Setup Parameters
    move.setup()

# move.move(50, direction = "forward", turn = "right")
# time.sleep(50)
# move.move(50, direction = "forward", turn = "left")
# time.sleep(50)
# move.motorStop()

    print(kp.getKey("s"))

    # Up Key
    if kp.getKey('UP'):
        move.move(50, direction = "forward", turn = "right")
        time.sleep(2)
        print(ultra.Ec)

    # Down Key
    if kp.getKey('DOWN'):    
        move.move(90, direction = "backward", turn = "left")
        time.sleep(2)

    # Left Key
    if kp.getKey('LEFT'):    
        move.move(90, direction = "forward", turn = "left")
        time.sleep(2)

    # Right Key
    if kp.getKey('RIGHT'):    
            move.move(90, direction = "backward", turn = "right")
            time.sleep(2)


if __name__ == "__main__":
    while True:
        main()
