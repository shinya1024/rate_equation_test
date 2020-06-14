from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def bibunn(t,z,a,b,c,d):
	 x, y = z
	 return [-a*x +b*y, c*x - d*y]

sol = solve_ivp(bibunn, [0,15], [0.4, 0.6], args=(2000, 1000, 2000, 1000),
                 dense_output=True)

t = np.linspace(0,15,3)


z = sol.sol(t)

plt.plot(t,z.T)
plt.xlabel('t')
plt.legend(['x','y'],shadow = True)
plt.title('System')
plt.xlim([0,15])
plt.ylim([0,1])
#plt.show()

plt.savefig('bibunn2.png')