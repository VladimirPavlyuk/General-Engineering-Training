import RPi.GPIO as GPIO
import time
DAC = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
troyka = 17
comparator = 4
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)
GPIO.output(troyka, 1)

for pin in DAC: GPIO.setup(pin, GPIO.OUT, initial = GPIO.HIGH)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def ADC():
    while True:
        for value in range(256):
            for i in range(len(DAC)):
                GPIO.output(DAC[i], decimal2binary(value)[i])
            time.sleep(0.001)
            voltage = (value / 256) * 3.3
            comparator_value = GPIO.input(comparator)
            if comparator_value == 0:
                print ('ADC value =', value, 'ADC voltage = ', voltage, ' ')
                break
    

try:
    ADC()
         
finally:
    for pin in DAC: GPIO.output(pin, 0)