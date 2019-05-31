import numpy as np
import matplotlib.pyplot as plt


N = 100
for _ in range(5):
    x = np.random.normal(0, 1, N)
    y = np.random.normal(2, 3, N)

    plt.hist(x, alpha=0.5, label='x')
    plt.hist(y, alpha=0.5, label='y')
    plt.legend(loc='upper right')
    plt.show()
