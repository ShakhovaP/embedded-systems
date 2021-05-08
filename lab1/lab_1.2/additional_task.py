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

def math_expectation(signal):
    return sum(signal)/ticks

def corelation(s1, s2):
    corelation = []
    for tau in range(max_tau):
        cov = 0
        # n = ticks-range_tau
        for t in range(max_ticks):
            cov += (s1[t] - math_expectation(s1))*(s2[t+tau] - math_expectation(s2))
        corelation.append(cov/max_ticks)
    return corelation

def plot_time(N, t1, t2):
    
    fig = plt.figure(figsize=(12, 6))
    s1 = fig.add_subplot(121)
    s2 = fig.add_subplot(122)

    s1.set_title('Час обчислення кореляції при різних N')
    s1.set_xlabel('кількість дискретних відліків')
    s1.set_ylabel('час обчислення')
    s1.plot(N, t1, '#4B0082')

    s2.set_title('Час обчислення автокореляції при різних N')
    s2.set_xlabel('кількість дискретних відліків')
    s2.set_ylabel('час обчислення')
    s2.plot(N, t2, '#FF00FF')
    plt.show()

min_t = 100
max_t = 1000
times_cor = []
times_autocor = []
N = []

for t in range(min_t, max_t+1, 100):
    signal_test1 = generate_signal(t)
    signal_test2 = generate_signal(t)
    max_tau = math.floor(t/2)
    max_ticks = max_tau
    N.append(t)

    start_time_cor = time.perf_counter()
    corelation(signal_test1, signal_test2)
    end_time_cor = time.perf_counter()
    times_cor.append(end_time_cor - start_time_cor)

    start_time_autocor = time.perf_counter()
    corelation(signal_test1, signal_test1)
    end_time_autocor = time.perf_counter()
    times_autocor.append(end_time_autocor - start_time_autocor)

plot_time(N, times_cor, times_autocor)

