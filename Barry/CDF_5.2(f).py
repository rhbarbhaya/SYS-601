import matplotlib.pyplot as plt 
import numpy as np


x = np.linspace(0, 5, 300)
y = 1 - 2.718**(-0.5 * x)

plot1 = plt.plot(0.21, 0.1, 'go')
plot2 = plt.plot(1.386, 0.5,'go')
plot3 = plt.plot(4.605, 0.9,'go')

plt.plot(x,y)
plt.axis([0,6,0,1])
plt.show()