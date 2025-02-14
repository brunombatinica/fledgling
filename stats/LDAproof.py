# testing the matrix multiplication that is happening

import numpy as np

x = np.array([1,3])
y = np.array([6,2])

sigma = np.array([[1, 2], [2, 1]])

print(x)
print(y)
print(sigma)


print(x.T @ sigma @ y)
print(y.T @ sigma @ x)

print(x.T@sigma@x - y.T@sigma@y)
print( (x-y).T @ sigma @ (x + y))