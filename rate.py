from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def rate(t,v,k1,k2,k3):
	 w, x, y, z = v
	 return [k2*y - (k1 + k3)*w, k2*y + k3*(w + y),k1*z*w - (k2 + k3)*y,- k1 * z]
	 
t_min = 0
t_max = 1.0*10e23
winit = 0.1
xinit = 0.2
yinit = 0.3
zinit = 0.4

sol = solve_ivp(rate, [t_min,t_max], [winit, xinit, yinit, zinit], args=(1.4*10**(-22),1.6*10**(-15),1.8*10**(-15)),t_eval = np.linspace(t_min,t_max,10000),method = "Radau")




plt.plot(sol.t,sol.y.T)
plt.xlabel('t')
plt.legend(['w','x','y','z'],shadow = True)
plt.title('System')
plt.xscale('log')
#plt.yscale('log')
plt.xlim([10e12,10e23])
#plt.ylim([0,0.3])
plt.show()
