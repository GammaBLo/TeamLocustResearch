import matplotlib.pyplot as plt
import numpy as np
import math

pi = calculate_pi_using_CBFs(100000)
x = 1
y = 2
z = 3
phi = 1.618  # Golden ratio
alpha = 0.5
omega = 2 * math.pi  # Frequency of 1 Hz
t = 0.5  # Time in seconds

def f(x, y, z, phi, alpha, omega, t):
    return phi**(x + y + z) + alpha * phi**(x + y + z) * math.cos(omega * t)

t_values = np.linspace(0, 10, 100)  # Generate 100 values from 0 to 10
results = [f(x, y, z, phi, alpha, omega, t) for t in t_values]

plt.plot(t_values, results)
plt.xlabel('Time (t)')
plt.ylabel('f(x, y, z)')
plt.title('Plot of f(x, y, z) over time')

def calculate_pi_using_CBFs(n):
    """Calculates the value of pi using CBFs.

    Args:
        n: The number of terms to use in the calculation.

    Returns:
        The value of pi, calculated using CBFs.
    """

    sum = 0
    for i in range(n):
        sum += CBF(i)

    return sum

def CBF(n):
    """Returns the CBF number for the given index.

    Args:
        n: The index of the CBF number.

    Returns:
        The CBF number for the given index.
    """

    return alpha * phi * π * psi * (1 + n)

def main():
    """Calculates the value of pi using CBFs and prints the results."""

    
    print("The value of pi is:", pi)

if __name__ == "__main__":
    main()

plt.show()
