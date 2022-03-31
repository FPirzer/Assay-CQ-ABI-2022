import numpy as np

# Number of rows, numbers of coloums
print(np.zeros((5, 5)))
print(np.ones((2, 4)))
print(np.arange(25))
print("Reshape:\n", np.arange(30).reshape(6, 5))
print("Transpose:\n", np.arange(30).reshape(6, 5).transpose())
print("Sum:", np.arange(30).reshape(6, 5).transpose().sum())
print("Min value:", np.arange(30).reshape(6, 5).transpose().min())
print("Max value:", np.arange(30).reshape(6, 5).transpose().max())
print("Shape:", np.arange(30).reshape(6, 5).transpose().shape)
