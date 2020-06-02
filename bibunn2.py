
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(x,t,a):
    dxdt = - a * x
    return dxdt

a = 1
x0 = 1
t = np.arange(0,100,0.01)
x = np.arange(0,100,0.01)

x = odeint(func,x0,t,args=(a,))

plt.plot(t,x,label = 'exp')

plt.legend()

plt.show()
