

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(x,t,a):
    dxdt = -a * x
    return dxdt

x0 = 100

t = np.linspace(0,100)

a = 0.1
x1 = odeint(model,x0,t,args=(a,))
a = 0.2
x2 = odeint(model,x0,t,args=(a,))
a = 0.5
x3 = odeint(model,x0,t,args=(a,))

plt.plot(t,x1,'r-',linewidth = 2,label = 'a = 0.1')
plt.plot(t,x2,'b--',linewidth = 2,label = 'a = 0.2')
plt.plot(t,x3,'g:',linewidth = 2,label = 'a = 0.5')

plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend()
#plt.show()

plt.savefig('bibunn.png')
