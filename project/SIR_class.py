# -*- coding: utf-8 -*-

import ODESolver
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import numpy as np

class ProblemSIR:
	def __init__(self, nu, beta, S0, I0, R0, T):
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
		
		self.S0 = S0
		self.I0 = I0
		self.R0 = R0
		self.T = T
	
	
	def __call__(self, u, t):
		"""Right-hand side function of the ODE system."""
		S, I, R = u
		return [-self.beta(t)*S*I,
		self.beta(t)*S*I-self.nu(t)*I,self.nu(t)*I]



class SolverSIR:
	def __init__(self, problem, dt):
		self.problem, self.dt = problem, dt
	def solve(self, method=ODESolver.RungeKutta4):
		self.solver = method(self.problem)
		ic = [self.problem.S0, self.problem.I0, self.problem.R0]
		self.solver.set_initial_condition(ic)
		n = int(round(self.problem.T/float(self.dt)))
		t = np.linspace(0, self.problem.T, n+1)
		u, self.t = self.solver.solve(t)
		self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]
	def plot(self):
		# plot S(t), I(t), and R(t)
		plt.plot(self.t,self.S,self.t,self.I,self.t,self.R)
		plt.ylabel('Population')
		plt.xlabel('Nr. of days')
		plt.legend(['S','I','R'], loc = 'best')
		plt.show()


beta = lambda t: 0.0005 if t <= 12 else 0.0001
#beta = 0.0005
nu = 0.1
S0 = 1500
I0 = 1
R0 = 0
T = 60
dt = 0.5

problem = ProblemSIR(nu, beta, S0, I0, R0, T)
solver = SolverSIR(problem, dt)
solver.solve()
solver.plot()



"""
For tilfellet når beta er avhengig av tiden, får vi at det det største antallet av mennesker som har blitt infisert er ca. 740, mens i tilfellet når beta = 0.0005 får vi at the største antallet av infiserte menneseker er ca. 900. 

"""

# Kjoreeksempel
"""
"""
