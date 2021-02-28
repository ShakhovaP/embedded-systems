import random
import math
import matplotlib.pyplot as plt
import time

n = 6
delta_w = 2100/n
ticks = 256
w = []
signal = []
min_ticks = 1000
max_ticks = 10000
times = []

for i in range(1, n + 1):
    w.append(delta_w*i)

for i in range(min_ticks, max_ticks+1, 100):
    for t in range(ticks):
        x = []
        for i in range(n):
            a = random.random()
            fi = random.random()

            xi = a*math.sin(w[i]*t+fi)
            x.append(xi)
        signal.append(sum(x))

    start = time.perf_counter()
    m = sum(signal)/ticks
    d = 0

    for s in signal:
        d += math.pow((s - m), 2)
    d = d/ticks
    end = time.perf_counter()
    times.append(end-start)

plt.plot(range(min_ticks, max_ticks +1, 100), times, color = '#00FFFF')
plt.xlabel('Кількість дискретних відліків ') 
plt.ylabel('Час обчислення')
plt.title('Графік залежності складності обчислень від часу') 
plt.show()
