import random
import math
import matplotlib.pyplot as plt
import time
import numpy as np

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


def fourier_transform(signal):
    N = len(signal)
    w0 = 2*math.pi/N
    res = []
    
    for p in range(N):
        f = 0
        for k in range(N):
            w_num = w0*p*k
            w = math.cos(w_num) - math.sin(w_num)*1j
            f += signal[k]*w
        res.append(abs(f))
    return res

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

def plot_time(x, t1, t2, t3):
    plt.plot(x, t1, color ='#9900CC')
    plt.text(100, 0.9, 'dft', color ='#9900CC')

    plt.plot(x, t2, color ='#0000CC')
    plt.text(100, 0.8, 'fft', color ='#0000CC')

    plt.plot(x, t3, color ='#FF0066')
    plt.text(100, 0.7, 'numpyfft', color ='#FF0066')

    plt.xlabel('кількість дискретних відліків') 
    plt.ylabel('час обчислення')
    plt.title('Час виконання dft, fft та numpyfft') 
    plt.show()

min_ticks = 100
max_tick = 1000
times_dft = []
times_fft = []
times_numpyfft = []
N = []

for t in range(min_ticks, max_tick+1, 100):
    signal_test = generate_signal(t)
    N.append(t)

    start_time_dft = time.perf_counter()
    fourier_transform(signal_test)
    end_time_dft = time.perf_counter()
    times_dft.append(end_time_dft - start_time_dft)

    start_time_fft = time.perf_counter()
    fast_fourier_transform(signal_test)
    end_time_fft = time.perf_counter()
    times_fft.append(end_time_fft - start_time_fft)

    start_time_numpyfft = time.perf_counter()
    np.fft.fft(signal_test)
    end_time_numpyfft = time.perf_counter()
    times_numpyfft.append(end_time_numpyfft - start_time_numpyfft)

plot_time(N, times_dft, times_fft, times_numpyfft)
