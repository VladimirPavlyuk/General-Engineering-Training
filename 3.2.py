import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setwarnings(False)

RPi.GPIO.setup(13, RPi.GPIO.OUT)

RPi.GPIO.output(13, 1)
time.sleep(3)

RPi.GPIO.output(13, 0)
time.sleep(3)

RPi.GPIO.output(13, 1)
time.sleep(3)

RPi.GPIO.output(13, 0)
time.sleep(3)

RPi.GPIO.output(13, 1)
time.sleep(3)

RPi.GPIO.output(13, 0)
time.sleep(3)
