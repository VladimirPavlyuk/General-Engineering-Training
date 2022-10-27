import RPi.GPIO
import time

RPi.GPIO.setwarnings(False)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

RPi.GPIO.setmode(RPi.GPIO.BCM)

for pin in leds: RPi.GPIO.setup(pin, RPi.GPIO.OUT)    

for i in range(3):
    for pin in leds:
        RPi.GPIO.output(pin, 1)
        time.sleep(0.2)
        RPi.GPIO.output(pin, 0)
        
for pin in leds: RPi.GPIO.output(pin, 0)
RPi.GPIO.cleanup()
