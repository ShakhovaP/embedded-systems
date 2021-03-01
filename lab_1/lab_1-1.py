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


for i in range(1, n + 1):
    w.append(delta_w*i)
    a.append(random.random())
    fi.append(random.random())


for t in range(ticks):
    x = []
    for i in range(n):
        xi = a[i]*math.sin(w[i]*t+fi[i])
        x.append(xi)
    signal.append(sum(x))

start = time.perf_counter()
m = sum(signal)/ticks
d = 0

for s in signal:
    d += math.pow((s - m), 2)
d = d/ticks
end = time.perf_counter()

print('Математичне очікування: ', m)
print('Дисперсія: ', d)
print('Час обчислення: ', end - start)

plt.plot(range(1, ticks + 1), signal, color = '#00FFFF')
plt.xlabel('час') 
plt.ylabel('сигнал')
plt.title('Графік залежності згенерованого випадкового сигналу від часу')
plt.show()

