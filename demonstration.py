import numpy as np
import clopy as cl

# create random matrix with made-up probabilities
data = np.matrix(np.random.random(100)).reshape(20, 5)
# set up file to store inequality matrices
output = np.zeros((data.shape[0], data.shape[1], data.shape[1]), dtype = int)

# create all inequality matrices 
for i in range(data.shape[0]):
    probabilities = np.asarray(data[i, :])
    output[i] = cl.imac(probabilities.squeeze(), thresholds = [0.1, -0.1])

print(output)