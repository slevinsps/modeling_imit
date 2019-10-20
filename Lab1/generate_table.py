import numpy as np

np.savetxt('table.txt', 
            np.random.randint(low=100000, high=1000000, size=(20000, 10)), 
            delimiter=' ', 
            fmt='%d')