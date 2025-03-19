import numpy as np

X = np.array([1,2,3,2,1])
H = np.array([4])

Y = np.convolve(X, H)

print(Y)