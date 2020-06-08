from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def bibunn(t,z,a,b,c,d):
	 x, y = z
	 return [-a*x +b*y, c*x - d*y]
sol = solve_ivp(bibunn, [0, 15], [10, 5], args=(15, 10, 30, 10),
                 dense_output=True)

t = np.linspace(0,15,300)


z = sol.sol(t)

plt.plot(t,z.T)
plt.xlabel('t')
plt.legend(['x','y'],shadow = True)
plt.title('System')
#plt.show()

plt.savefig('bibunn1.png')