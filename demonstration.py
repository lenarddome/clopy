import numpy as np
import pandas as pd
import datatable as dt

data = np.matrix(np.random.random(100)).reshape(20, 5)
output = np.zeros((data.shape[0], data.shape[1], data.shape[1]), dtype = int)

for i in range(data.shape[0]):
    probabilities = np.asarray(data[i, :])
    output[i] = imac(probabilities.squeeze(), thresholds = [0.1, -0.1])

print(output)
names(output)