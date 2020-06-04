from scipy.integrate import solve_ivp

def upward_cannon(t,y):
    return [y[1],-0.5]
def hit_ground(t,y):
    return y[0]

hit_ground.terminal = True
hit_ground.direction = -1

sol = solve_ivp(upward_cannon,[0,100],[0,10],events = hit_ground)

print(sol.t_events)
print(sol.t)