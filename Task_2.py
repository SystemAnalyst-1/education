import numpy as np

a = np.array([[1, 2, 3, 3, 1],
             [6, 8, 11, 10, 7]]).transpose()
mean_a = a.mean(axis =0)

a_centered = a - mean_a
print(a_centered)