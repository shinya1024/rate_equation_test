from scipy.integrate import solve_ivp

def exponetial_decay(t,y):
    return -0.5 * y
sol = solve_ivp(exponetial_decay,[0,10],[2,4,8],t_eval=[0,1,2,4,10])
print(sol.t)
print(sol.y)