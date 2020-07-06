import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-10, 10, 0.05)
Y = np.arange(-10, 10, 0.05)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
ax.plot_surface(X, Y, R, cmap='rainbow')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.show()
