import RPi.GPIO as GPIO
import time
from matplotlib import pyplot as plt

DAC = [26, 19, 13, 6, 5, 11, 9, 10]
LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
troyka = 17
comparator = 4
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)
max_value = 255 
counter = 0
value_array = []
for pin in DAC: GPIO.setup(pin, GPIO.OUT, initial = GPIO.HIGH)
for pin in LEDS: GPIO.setup(pin, GPIO.OUT) 

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
                for i in range(len(LEDS)):
                    GPIO.output(LEDS[i], decimal2binary(value)[i])
                return (value)
                break

def ADC_2():
    L, R = 0, 255
    while L < R:
        x = L + (R - L) // 2
        for i in range(len(DAC)):
                GPIO.output(DAC[i], decimal2binary(x)[i])
        time.sleep(0.001)
        comparator_value = GPIO.input(comparator)
        if comparator_value == 0:
            R = x
        else:
            L = x + 1
    for i in range(len(LEDS)):
        GPIO.output(LEDS[i], decimal2binary(L)[i])
    return (L)

try:
    print('Начало эксперимента, t = 0 \n')
    GPIO.output(troyka, 1)
    t_1 = time.time()
    while(ADC_2() <= 255 * 0.97):
        value_array.append(ADC_2())
        counter += 1;
    t_2 = time.time()
    print('Конденсатор заряжен, t = ', t_2 - t_1, ' \n') 
    GPIO.output(troyka, 0)
    while(ADC_2() >= 255 * 0.02):
        value_array.append(ADC_2())
        counter += 1;
    t_3 = time.time()
    print('|Конденсатор разряжен, конце эксперимента, t = ', t_3 - t_1)


    # работа с файлами
    with open("data.txt", "w") as outfile_1:
        outfile_1.write("\n".join([str(item) for item in value_array]))
    with open("settings.txt", "w") as outfile_2:
        str_1 = 'Средняя чистота дискретизации ' + str(round((t_3 - t_1) / (counter - 1), 5)) + ' C'
        outfile_2.write(str_1)
        outfile_2.write('\n')
        str_2 = 'Шаг квантования АЦП ' + str(round(3.3 / 255, 5)) + ' В'
        outfile_2.write(str_2)
        
    print()


finally:
    for pin in DAC: GPIO.output(pin, 0)
    for pin in LEDS: GPIO.output(pin, 0)
    plt.plot(value_array)
    plt.show()
