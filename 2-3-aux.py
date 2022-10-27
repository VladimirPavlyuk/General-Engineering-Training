import RPi.GPIO
import time

LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
AUX = [22, 23, 27, 18, 15, 14, 3, 2]

RPi.GPIO.setwarnings(False)

RPi.GPIO.setmode(RPi.GPIO.BCM)

for pin in LEDS: RPi.GPIO.setup(pin, RPi.GPIO.OUT)
for pin in AUX: RPi.GPIO.setup(pin, RPi.GPIO.IN)

while True:
    for i in range(len(LEDS)):
        RPi.GPIO.output(LEDS[i], RPi.GPIO.input(AUX[i]))
     