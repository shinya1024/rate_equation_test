from scipy.integrate import solve_ivp

def upward_cannon(t,y):
    return [y[1],-0.5]
def hit_ground(t,y):
    return y[0]

hit_ground.terminal = True
hit_ground.direction = -1
def apex(t,y):
    return y[1]

sol = solve_ivp(upward_cannon,[0,100],[0,10],events = (hit_ground,apex),dense_output = True)

print(sol.t_events)
print(sol.t)
print(sol.sol(sol.t_events[1][0]))
print(sol.y_events)
