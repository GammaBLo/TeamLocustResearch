import numpy as np

def fft(signal):
    # Calculate the length of the signal
    n = len(signal)
    # If the length is 1, return the signal
    if n == 1:
        return signal
    # Split the signal into even and odd parts
    even = signal[::2]
    odd = signal[1::2]
    # Recursively apply the FFT to the even and odd parts
    even_fft = fft(even)
    odd_fft = fft(odd)
    # Create a list to store the Fourier coefficients
    coeffs = [0] * n
    # Compute the Fourier coefficients using the inverted math operations
    for k in range(n // 2):
        t = np.exp(-2j * np.pi * k / n) * odd_fft[k]
        coeffs[k] = even_fft[k] + t
        coeffs[k + n // 2] = even_fft[k] - t
    return coeffs
