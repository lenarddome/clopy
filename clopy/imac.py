import numpy as np;

def imac(probabilities, thresholds):
    dimension = len(probabilities);
    inequalities = np.zeros([dimension, dimension], dtype = float);
    for i in range(dimension):
        for j in range(dimension):
            if (i <= j):
                inequalities[i, j] = probabilities[i] - probabilities[j];
            else:
                inequalities[i, j] = 2;
    inequalities[(inequalities <= thresholds[0]) & (inequalities >= thresholds[1])] = 0;
    inequalities[(inequalities > thresholds[0]) & (inequalities < 2)] = 1;
    inequalities[(inequalities < thresholds[1]) & (inequalities < 2)] = -1;
    return inequalities.astype(int);

# imac(np.random.random(5), np.array([0.1, -0.1]))

# human = [imac(np.random.random(5), np.array([0.1, -0.1])),
#       imac(np.random.random(5), np.array([0.1, -0.1])),
#       imac(np.random.random(5), np.array([0.1, -0.1]))]
# machine = [imac(np.random.random(5), np.array([0.1, -0.1])),
#       imac(np.random.random(5), np.array([0.1, -0.1])),
#       human[0],
#       imac(np.random.random(5), np.array([0.1, -0.1])),
#       human[1]]