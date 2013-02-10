import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 10
mu, sigma = 0, n

s = np.random.normal(mu, sigma, 10000)
count, bins, ignored = plt.hist(s, 100, normed=True,alpha=0.5,color='g')

normX = norm.pdf(bins,0,n)
plt.plot(bins, normX, linewidth=2, color='r')
plt.title('Normal distribution')
plt.grid(True)
plt.show()

