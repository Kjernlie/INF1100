from math import pi

g = 9.81 # m/s**2
rho = 1.2 # kg / m**(-3)
a = 11*10**(-2) # m
m = 0.43 # kg
C_d = 0.4 # dimensionless
A = pi*a**2
V1 = 120/3.6 # m/s
V2 = 30/3.6 # m/s

def F_d(C_d,rho,A,V):
    return 0.5*C_d*rho*A*V**2

def F_g(m,g):
    return m*g

F_d_slow = F_d(C_d,rho,A,V2)
F_d_fast = F_d(C_d,rho,A,V1)
F_g = F_g(m,g)

print 'The Drag force is %.1f N for the fast case, and %.1f N for the slow case. The gravitational force is %.1f N. The ratio of the drag force and the gravitational force is %.1f for the fast case and %.1f for the slow case.' %(F_d_fast,F_d_slow,F_g,F_d_fast/F_g,F_d_slow/F_g)
