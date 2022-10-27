import RPi.GPIO as GPIO
DAC = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in DAC: GPIO.setup(pin, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


try:
    while True:
        voltage = 0.0
        number = int(input('Please enter a number from 0 to 255 \n'))
        if number < 0:
            print('Negative')
        elif number > 255:
            print('Number is too big')
        else:
            for i in range(len(DAC)):
                GPIO.output(DAC[i], decimal2binary(number)[i])
                voltage += (1 / (2 ** (i + 1))) * (3.3127) * decimal2binary(number)[i] 
            print ('Напряжение U = ', voltage)
except ValueError:
    print('Not integer')
           
finally:
    for pin in DAC: GPIO.output(pin, 0)
