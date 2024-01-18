import numpy as np
import matplotlib.pyplot as plt

def line1(start, end):
  """
  Returns a line that can be manipulated.

  Args:
    start: The starting point of the line.
    end: The end point of the line.

  Returns:
    A NumPy array of coordinates.
  """

  coordinates = np.zeros((2,))
  coordinates[0] = start
  coordinates[1] = end

  return coordinates

def line2(n):
  """
  Returns a zig zag pattern.

  Args:
    n: The number of points in the line.

  Returns:
    A NumPy array of coordinates.
  """

  coordinates = np.zeros((2 * n,))
  for i in range(n):
    coordinates[2 * i] = i
    coordinates[2 * i + 1] = i + 1

  return coordinates

if __name__ == "__main__":
  start = 0
  end = 10
  coordinates1 = line1(start, end)
  plt.plot(coordinates1[:, 0], coordinates1[:, 1])

  n = 10
  coordinates2 = line2(n)
  plt.plot(coordinates2[:, 0], coordinates2[:, 1])

  plt.show()
