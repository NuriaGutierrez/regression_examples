import numpy as np
import matplotlib.pyplot as plt

def f(num_samples, noise=0):
    #x = np.random.rand(num_samples)*2*np.pi
    x = np.random.rand(num_samples)*3

    x.sort()
    #y = np.exp(np.sin(x))
    #y = np.sin(np.exp(x))
    y = np.exp(x)*np.sin(20*x)
    y += np.random.randn(num_samples)*noise
    return (x,y)

x,y = f(1000,1)
plt.scatter(x,y)
