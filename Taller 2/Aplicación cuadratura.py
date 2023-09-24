import numpy as np
import matplotlib.pyplot as plt


#2
def P(v, T, M=0.00028, R=0.0813):
    return 100* 4 * np.pi * (( M / ( 2 * np.pi * R * T ))**(3/2)) * (v**2) * np.exp(-(M * (v**2))/( 2 * R * T))

v = np.linspace(0, 800, 10000)
plt.plot(v, P(v, 100), label = 'T=100')
plt.plot(v, P(v, 300), label = 'T=300')
plt.plot(v, P(v, 700), label = 'T=700')
plt.plot(v, P(v, 1000), label = 'T=1000')
plt.legend()
plt.show()
