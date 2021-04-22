import random
import math
import matplotlib.pyplot as plt
import time

n = 6
delta_w = 2100/n
ticks = 256

def generate_signal(ticks):
    w = []
    a = []
    fi = []
    signal = []

    for i in range(1, n + 1):
        w.append(delta_w*i)
        tmpA = []
        tmpFi = []
        for t in range(ticks):
            tmpA.append(random.random())
            tmpFi.append(random.random())
        a.append(tmpA)
        fi.append(tmpFi)

    for t in range(ticks):
        x = []
        for i in range(n):
            xi = a[i][t]*math.sin(w[i]*t+fi[i][t])
            x.append(xi)
        signal.append(sum(x))
    return signal

signal = generate_signal(ticks)


def fast_fourier_transform(x):
    N = len(x)
    middle = int(N/2)
    res = [0] * N

    if N <= 1: 
        return x
    
    x_even = fast_fourier_transform(x[::2])
    x_odd = fast_fourier_transform(x[1::2])

    for p in range(middle):
        w_num = p*2*math.pi/N
        w = math.cos(w_num) - math.sin(w_num)*1j
        res[p] =          x_even[p] + w*x_odd[p]
        res[middle + p] = x_even[p] - w*x_odd[p]
    
    return res

transformed_signal = fast_fourier_transform(signal)


def plot_transform(x):
    
    trans_x = fast_fourier_transform(x)
    for i in range(len(trans_x)):
        trans_x[i] = abs(trans_x[i])

    fig = plt.figure(figsize=(9, 7))
    s1 = fig.add_subplot(211)
    s2 = fig.add_subplot(212)

    s1.set_title('Графік згенерованого сигналу')
    # s1.set_xlabel('час')
    # s1.set_ylabel('сигнал')
    s1.plot(x, '#4B0082')

    s2.set_title('Графік перетвореного сигналу')
    s2.set_xlabel('час')
    s2.set_ylabel('сигнал')
    s2.plot(trans_x,'#FF00FF')
    plt.show()

plot_transform(signal)


def plot_time(x, times):
    plt.plot(x, times, color ='#8A2BE2')
    plt.xlabel('кількість дискретних відліків') 
    plt.ylabel('час обчислення')
    plt.title('Графік залежності складності обчислень від часу') 
    plt.show()


min_ticks = 100
max_tick = 1000
times = []
N = []

for t in range(min_ticks, max_tick+1, 100):
    signal = generate_signal(t)
    N.append(t)

    start_time = time.perf_counter()
    fast_fourier_transform(signal)
    end_time = time.perf_counter()
    times.append(end_time - start_time)

plot_time(N, times)