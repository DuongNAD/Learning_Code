from unittest import result

import numpy as np

if __name__ == '__main__':
    Array1 = np.array([0, 10 ,20 ,40, 60])
    Array2 = np.array([10, 30, 40])

    result = np.isin(Array1, Array2)
    print(result)