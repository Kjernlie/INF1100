# -*- coding: utf-8 -*-
import ODESolver
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import numpy as np

class ProblemSIR:
        def __init__(self, nu, beta, p,  S0, I0, R0, V0,  T):
                """
                nu, beta: parameters in the ODE system
                S0, I0, R0: initial values
                T: simulation for t in [0,T]
                """
                if isinstance(nu, (float,int)): # number?
                        self.nu = lambda t: nu
                # wrap as function
                elif callable(nu):
                        self.nu = nu
                # same for beta and self.beta

                if isinstance(beta, (float,int)):
                        self.beta = lambda t: beta
                elif callable(beta):
                        self.beta = beta
		
		self.p = p
                self.S0 = S0
                self.I0 = I0
                self.R0 = R0
		self.V0 = V0
                self.T = T
		
        
        
        def __call__(self, u, t):
                """Right-hand side function of the ODE system."""
                S, I, R, V = u
                return [-self.beta(t)*S*I-self.p*S,
                self.beta(t)*S*I-self.nu(t)*I,self.nu(t)*I,
		self.p*S]
                


class SolverSIR:
        def __init__(self, problem, dt):
                self.problem, self.dt = problem, dt
        def solve(self, method=ODESolver.RungeKutta4):
                self.solver = method(self.problem)
                ic = [self.problem.S0, self.problem.I0, 
		self.problem.R0, self.problem.V0]
                self.solver.set_initial_condition(ic)
                n = int(round(self.problem.T/float(self.dt)))
                t = np.linspace(0, self.problem.T, n+1)
                u, self.t = self.solver.solve(t)
                self.S, self.I, self.R, self.V = \
		u[:,0], u[:,1], u[:,2], u[:,3]
        def plot(self):
                plt.plot(self.t,self.S,
		self.t,self.I,self.t,self.R, self.t, self.V)
                plt.ylabel('Population')
                plt.xlabel('Nr. of days')
                plt.legend(['S','I','R', 'V'], loc = 'best')
                plt.show()


beta = 0.0005
nu = 0.1
p = 0.1
S0 = 1500
I0 = 1
R0 = 0
V0 = 0
T = 60
dt = 0.5

problem = ProblemSIR(nu, beta, p,  S0, I0, R0, V0, T)
solver = SolverSIR(problem, dt)
solver.solve()
solver.plot()


"""
Vi ser at antallet infiserte er mye lavere her (max. infiserte ca. 60), enn for tilfellet uten vaksiner (max. infiserte ca. 900).
"""


# Kjoreeksempel
"""

""" 
