from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def rate(t,v,k1,k2,k3):
	 w, x, y, z = v
	 return [k2*y - (k1 + k3)*w, k2*y + k3*(w + y),k1*z*w - (k2 + k3)*y,-k1*z]
t_min = 0
t_max = 15000000000000000
winit = 0.4
xinit = 0.2
yinit = 0.3
zinit = 0.1
sol = solve_ivp(rate, [t_min,t_max], [winit, xinit, yinit, zinit], args=(0.000000000000000000000014,0.0000000000000003,0.0000000000000012),t_eval = np.linspace(t_min,t_max,1000))





plt.plot(sol.t,sol.y.T)
plt.xlabel('t')
plt.legend(['w','x','y','z'],shadow = True)
plt.title('System')
#plt.xlim([0,0.8])
#plt.ylim([0,1])
plt.show()
