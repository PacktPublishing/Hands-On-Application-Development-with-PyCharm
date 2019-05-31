import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% generate sample data
# x and z are randomly generated
# y is loosely two times of x
x = np.random.rand(50,)
y = x * 2 + np.random.normal(0, 0.3, 50)
z = np.random.rand(50,)

df = pd.DataFrame({
    'x': x,
    'y': y,
    'z': z
})

#%% compute the correlation matrix
corr_mat = df.corr()

#%% plot the heatmap
plt.matshow(corr_mat)
plt.show()
