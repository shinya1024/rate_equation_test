from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def bibunn(t,z,a,b,c,d):
	 x, y = z
	 return [-a*x +b*y, c*x - d*y]
t_min = 0
t_max = 15
xinit = 0.4
yinit = 0.6
sol = solve_ivp(bibunn, [t_min,t_max], [xinit, yinit], args=(1, 2, 1, 2),t_eval = np.linspace(t_min,t_max,1000))






plt.plot(sol.t,sol.y.T)
plt.xlabel('t')
plt.legend(['x','y'],shadow = True)
plt.title('System')
plt.xlim([0,2])
plt.ylim([0,1])
plt.show()

#plt.savefig('bibunn2.png')