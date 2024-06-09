import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial as P
from random import shuffle

def function_1(n: int) -> None:
    temp_list = list()
    for i in range(n**2):
        temp = 0
        for j in range(i):
            temp += j
        temp_list.append(temp)
    sum(temp_list)

def function_2(n: int) -> None:
    print(n)
    for i in range(n):
        temp_list = [j + i for j in range(n)]
        shuffle(temp_list)
        max(temp_list)

def measure_time(func, n_values, trials=3):
    times = []
    for n in n_values:
        start_time = time.time()
        for _ in range(trials):
            func(n)
        elapsed = (time.time() - start_time) / trials
        times.append(elapsed)
    return times

# Measure time for function_1
n_values_1 = [10, 20, 30, 40, 50]
times_1 = measure_time(function_1, n_values_1)

# Measure time for function_2
n_values_2 = [100, 200, 300, 400, 500]
times_2 = measure_time(function_2, n_values_2)

# Convert n_values to numpy arrays for polynomial fitting
n_values_1 = np.array(n_values_1)
n_values_2 = np.array(n_values_2)

# Fit polynomial to the times
poly_1 = P.fit(n_values_1, times_1, 4)  # function_1: degree 4
poly_2 = P.fit(n_values_2, times_2, 2)  # function_2: degree 2

# Plot the results
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(n_values_1, times_1, 'o', label='Measured times')
plt.plot(n_values_1, poly_1(n_values_1), '-', label='Fitted polynomial (degree 4)')
plt.title('function_1 Time Complexity')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(n_values_2, times_2, 'o', label='Measured times')
plt.plot(n_values_2, poly_2(n_values_2), '-', label='Fitted polynomial (degree 2)')
plt.title('function_2 Time Complexity')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()

plt.tight_layout()
plt.show()
