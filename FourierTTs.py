import numpy as np
import time
from IntrovertFourier import fft as my_fft_function  # import your function from IntrovertFourier.py

# Generate a test signal
n = 1024  # signal length
dt = 0.01  # time step
t = np.arange(n) * dt  # time array
f = 10.0  # signal frequency
signal = np.sin(2 * np.pi * f * t)  # input signal

# Apply standard FFT algorithm (numpy.fft.fft) and measure execution time
start_time = time.time()
result_1 = np.fft.fft(signal)
execution_time_1 = time.time() - start_time

from IntrovertFourier import fft as my_fft_function  # import your function from IntrovertFourier.py

# Apply IntrovertFourier algorithm and measure execution time
start_time = time.time()
result_2 = my_fft_function(signal)
execution_time_2 = time.time() - start_time


# Compare the results and execution times
if np.allclose(result_1, result_2):
    print("The results are the same")
else:
    print("The results are different")

print(f"Execution time of standard FFT algorithm: {execution_time_1:.4f} seconds")
print(f"Execution time of IntrovertFourier algorithm: {execution_time_2:.4f} seconds")
