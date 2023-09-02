import numpy as np

def sigmoid(t):
    return 1 / (1 + np.exp(-t))

# Assume t is the linear combination of input variables
t = np.array([1, 2, 3])
probability = sigmoid(t)

print(probability)

