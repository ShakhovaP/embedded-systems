import random
import math
import matplotlib.pyplot as plt
import time

n = 6
delta_w = 2100/n
ticks = 256
max_tau = 175
max_ticks = 75

def generate_signal():
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
    return signal

signal_x = generate_signal()
signal_y = generate_signal()

def show_signal(s1, s2):
    plt.plot(range(1, ticks + 1), s1, color = '#00FFFF')
    plt.plot(range(1, ticks + 1), s2, color = '#0000FF')
    plt.xlabel('час') 
    plt.ylabel('сигнал')
    plt.title('Графік залежності згенерованого випадкового сигналу від часу')
    plt.show()

show_signal(signal_x, signal_y)

def math_expectation(signal):
    return sum(signal)/ticks

def deviation(signal):
    d = 0
    for s in signal:
        d += math.pow((s - math_expectation(signal)), 2)
    return d/ticks

def corelation(s1, s2):
    corelation = []
    for tau in range(max_tau):
        cov = 0
        # n = ticks-range_tau
        for t in range(max_ticks):
            cov += (s1[t] - math_expectation(s1))*(s2[t+tau] - math_expectation(s2))
        corelation.append(cov/max_ticks)
    
    if s1==s2:
        prefix = 'авто'
    else:
        prefix = ''

    plt.plot(range(max_tau), corelation, color = '#00FFFF')
    plt.xlabel('tau')    
    plt.ylabel('%sкореляція'%prefix)
    plt.title('Графік залежності %sкореляції від випробувального інтервалу tau'%prefix)
    plt.show()

corelation(signal_x, signal_x)
corelation(signal_x, signal_y)
