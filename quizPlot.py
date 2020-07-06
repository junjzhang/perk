import matplotlib.pyplot as plt
import numpy as np

colorMap = ['lightcoral', 'salmon', 'coral',
            'sandybrown', 'y', 'limegreen', 'lightseagreen']
plt.figure(figsize=(12, 8))
x = np.arange(-150, 200)*0.05
y = (2-x)**2+(3.1-2*x)**2+(3.3-3*x)**2+(4.9-4*x)**2
plt.plot(x, y, color=colorMap[0], label=r"$h(a)$")
plt.legend()
plt.xlabel(r'$a$', fontsize=12)
plt.show()
