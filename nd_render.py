import numpy as np
import matplotlib.pyplot as plt

n = -50.0
m = abs(n)
x = np.arange(n, m, 1)
y = (1/np.sqrt(2*np.pi) * np.exp(-(x**2)/(10*m)))*20

#np.clip(y, 0, 6,out=y)
plt.title('Clamp normal distribution')
plt.axis([n, m, 0, 10])
plt.bar(x, y, align = 'center',width = 1,color='b',edgecolor='white',alpha=0.5)

plt.grid(True)
plt.plot(x, y, linewidth=2, color='r')
plt.show()
