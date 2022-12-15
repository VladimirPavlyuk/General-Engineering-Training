from re import U
from xml.dom.expatbuilder import TEXT_NODE
import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt('data.txt', dtype=float)
f, q = np.loadtxt('settings.txt', dtype = float)

figure, axes = plt.subplots(figsize=(16, 10))

axes.minorticks_on()
axes.grid(which='major', linestyle='-', linewidth=0.5)     
plt.grid(which='minor', linestyle='--', linewidth=0.25)

axes.set_title('Процесс зарядки и разрядки конденсатора в RC-цепочке')
axes.set_ylabel('Напряжение, В')
axes.set_xlabel('Время, с')

t_min = 0
t_max = len(data) * f

U_min = data.min() * q
U_max = data.max() * q

axes.set_xlim((t_min), (t_max * 1.05))
axes.set_ylim(U_min * 0.95, U_max * 1.05)

time = np.linspace(t_min, t_max, len(data))

charging_time = data.argmax() * f
discharging_time = (len(data) - data.argmax()) * f

TEXT_1 = f'Время зарядки: {charging_time:.1f}'
TEXT_2 = f'Время разрядки: {discharging_time:.1f}'
axes.text(t_max * 0.8, U_max * 0.8, TEXT_1)
axes.text(t_max * 0.8, U_max * 0.75, TEXT_2)
axes.plot(time, data * q)
axes.legend
figure.savefig('U(t).svg')
plt.show()



