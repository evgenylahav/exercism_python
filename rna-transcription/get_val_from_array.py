import numpy as np


input_array = np.array([[1, 2, 3, 4, 5], [11, 22, 33, 44, 55], [111, 222, 333, 444, 555]])
r = np.array([0, 1, 0, 2])
c = np.array([0, 2, 4, 3])

expected_result = np.array([1, 33, 5, 444])
actual_result = input_array[r, c]

print(expected_result)
print(actual_result)
