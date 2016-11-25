import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4

def f(u,t): # Function with system of ODEs
    # S'(t) = -beta*S*I
    # I'(t) = beta*S*I - nu*I
    # R'(t) = nu*I
    S, I, R = u
    nu = 0.1
    beta = 0.0005
    return [-beta*S*I, beta*S*I - nu*I, nu*I]

def plotSIR(t,S,I,R): # Function for plotting
    plt.figure()
    plt.plot(t,S,t,I,t,R)
    plt.ylabel('Number of people')
    plt.xlabel('Time (days)')
    plt.legend(['S','I','R'],loc='right')
    plt.show()

def terminate(u,t,step_no): # Terminate solver if S + I + R is not constant
    eps = 1.0E-06
    S = u[step_no,0]; I = u[step_no,1]; R = u[step_no,2]
    S0 = u[0,0]; I0 = u[0,1]; R0 = u[0,2]
    N0 = S0 + I0 + R0
    N = S + I + R
    return abs(N0-N) > eps

# t=0; setting initial coniditions
S = 1500 # number of susceptibles
I = 1    # number of infected
R = 0    # number of recovered
U0 = [S,I,R]

# Defining time range
t0 = 0; t_end = 60; dt = 0.5
time_points = np.linspace(t0,t_end,t_end/dt + 1)

# Setting up solver and solving
solver = RungeKutta4(f)
solver.set_initial_condition(U0)
u, t = solver.solve(time_points,terminate)
print u

# Getting back variables
#S = u[:,0]; I = u[:,1]; R = u[:,2]

# Plotting
#plotSIR(t,S,I,R)

"""
Kjoreeksempel
> python SIR.py

Kommentar til endring av beta:
Med beta=0.0001 til forskjell fra beta=0.0005 er det to ting som skiller seg:
Det ene er at tiden det tar foer det er et maksimalt antall smittede kommer mye
senere, ved omtrent t=120 dager. Det andre er at det blir langt faerre smittede,
og ved sykdommens slutt har bare ca 900 personer blitt smittet, til forskjell
fra alle 1500 med beta=0.0005.
"""
