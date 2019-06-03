import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Generate sample data
x = np.random.rand(50,)
y = x * 2 + np.random.normal(0, 0.3, 50)
z = np.random.rand(50,)

df = pd.DataFrame({
    'x': x,
    'y': y,
    'z': z
})

# Compute and show correlation matrix
corr_mat = df.corr()

plt.matshow(corr_mat)
plt.show()

# Plot x and y
plt.scatter(df['x'], df['y'])
plt.show()
