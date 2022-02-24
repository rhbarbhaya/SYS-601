import matplotlib.pyplot as plt 
import numpy as np
x1 = np.linspace(0.5, 1.5, 50)
y1 = 0.25*x1**2 - 0.25*x1 + 0.0625

x2 = np.linspace(1.5,2.5,500)
y2 = 0.5*x2- 0.5

x3 = np.linspace(2.5,3.5, 500)
y3 = -0.25*x3**2 +1.75*x3 -2.0625

plt.plot(x1,y1,x2,y2,x3,y3)
plt.axis([0,4,0,1.2])
plt.show()