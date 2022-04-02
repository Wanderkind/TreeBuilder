import matplotlib.pyplot as plt
import numpy as np

x = np.array([2.5,2.9,3.0,3.1,3.5,3.6,3.6,3.7,3.9,4.1,4.2,4.4,2.5,2.8,3.0,2.9,3.4])
y = np.array([2.4,2.6,3.1,3.3,3.4,3.3,3.7,3.9,3.8,3.9,4.0,4.2,2.6,2.9,3.0,2.8,3.2])
plt.scatter(x,y)

x = np.array([2.2])
y = np.array([3.9])
plt.scatter(x,y)

x = np.array([1.4])
y = np.array([1.4])
plt.scatter(x,y)

plt.show()
