import RPi.GPIO
import time

RPi.GPIO.setwarnings(False)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = []
for i in range(8):
    number.append(0)

RPi.GPIO.setmode(RPi.GPIO.BCM)

for pin in dac: RPi.GPIO.setup(pin, RPi.GPIO.OUT)

for bit in range(len(number)):
    number[bit] = int(input())

for i in range(len(dac)):
        RPi.GPIO.output(dac[i], number[i])

time.sleep(15)

for pin in dac: RPi.GPIO.output(pin, 0)
RPi.GPIO.cleanup()
