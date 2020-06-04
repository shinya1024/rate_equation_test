from scipy.integrate import solve_ivp
import numpy as np

def bibunn(t,z,a,b,c,d):
	 x, y = z
	 return [-a*x +b*y, c*x - d*y]
sol = solve_ivp(bibunn, [0, 15], [10, 5], args=(1.5, 1, 3, 1),
                 dense_output=True)

t = np.linspace(0,15,300)
z = sol.sol(t)
import matplotlib.pyplot as plt
plt.plot(t,z.T)
plt.xlabel('t')
plt.legend(['x','y'],shadow = True)
plt.title('Lotka-Volterra System')
plt.show()
