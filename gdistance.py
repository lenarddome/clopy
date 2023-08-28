import numpy as np

def gdistance(human, model, universal, weight, frequencies, xtdo):

    ## define some classes for improving function output and print handling
    class organize:
        def __init__(self, distance, alpha, beta, accommodation):
            self.distance = distance;
            self.alpha = alpha;
            self.beta = beta;
            self.accommodation = accommodation;
        
        def distance(self):
            return self.distance;
        def alpha(self):
            return self.alpha;
        def beta(self):
            return self.beta;
        def accommodation(self):
            return self.accommodation;
        
        def __str__(self):
            return "gdistance: " + str(self.distance) + "\nalpha: " + str(self.alpha) + "\nbeta: " + str(self.beta);
        
        def show(self):
            print("gdistance: " + str(self.distance) + "\nalpha: " + str(self.alpha) + "\nbeta: " + str(self.beta));

    ## calculate g-distance
    hlength = len(human);
    mlength = len(model);
    accommodation = np.zeros((hlength, mlength)).astype(int);
    for i in range(hlength):
        for j in range(mlength):
            if (human[i] == model[j]).all():
                accommodation[i, j] = 1;
    weighted = accommodation.sum(1) * frequencies;
    alpha = weighted.sum();
    ump = np.count_nonzero(accommodation.sum(0) == 0);
    beta = ump/(universal - hlength);
    distance = np.sqrt(weight * (1 - alpha)**2 + (1 - weight) * (beta)**2);
    
    ## return output
    if xtdo:
        return organize(distance, alpha, beta, accommodation);
    else:
        return distance;

out = gdistance(human, model, 10, 0.5, frequencies = [0.3, 0.1, 0.6], xtdo = True)

out.show()
print(out)
out.distance
out.accommodation