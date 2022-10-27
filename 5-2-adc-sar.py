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
                

try:
    while True:
        for i in range(1, 8 + 1):
            voltage = 0
            value_counter = 0
            time.sleep(0.001)
            value = 128 // i
            comparator_value = GPIO.input(comparator)
            if comparator_value == 1:
                voltage += value / 256 * 3.3
                value_counter += value
            for i in range(len(DAC)):
                GPIO.output(DAC[i], decimal2binary(value)[i])
        print ('ADC value =', value, 'ADC voltage = ', voltage, ' ')


           
finally:
    for pin in DAC: GPIO.output(pin, 0)