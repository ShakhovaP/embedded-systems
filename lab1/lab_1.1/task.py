import random
import math
import matplotlib.pyplot as plt
import time

n = 6
delta_w = 2100/n
ticks = 256
w = []
a = []
fi = []
signal = []
div = []


for i in range(1, n + 1):
    w.append(delta_w*i)
    a.append(random.random())
    fi.append(random.random())


for t in range(1, ticks + 1):
    x = []
    for i in range(n):
        xi = a[i]*math.sin(w[i]*t+fi[i])
        x.append(xi)
    signal.append(sum(x))
    m = sum(signal)/t

    d = 0
    for s in signal:
        d += math.pow((s - m), 2)
    d = d/t
    div.append(d)

print('Дисперсія: ', d)


plt.plot(range(1, ticks + 1), div, color = '#00FFFF')
plt.xlabel('час') 
plt.ylabel('дисперсія')
plt.title('Графік залежності дисперсії від часу(кількості дискретних відліків)')
plt.show()

