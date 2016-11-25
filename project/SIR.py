# -*- coding: utf-8 -*-
from ODESolver import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

def SIR(u,t):
	S,I,R = u
	nu = 0.1
	beta = 0.0005 # beta = 0.0001
	return [-beta*S*I, beta*S*I - nu*I, nu*I]

def terminate(u, t, step_no):
	tol = 1e-8
	return abs(sum(u[step_no])-sum(u[0])) > tol

def plot_SIR(S,I,R,t):
	plt.plot(t,S,t,I,t,R)
	plt.ylabel('Population')
	plt.xlabel('Nr. of days')
	plt.legend(['S','I','R'], loc = 'best')
	plt.show()

S = 1500
I = 1
R = 0
U0 = [S,I,R]
t_inital = 0
t_final = 60 # t_final = 200
delta_t = 0.5
N = (t_final-t_inital)/delta_t
t_vec = np.linspace(t_inital, t_final, N+1)

solver = RungeKutta4(SIR)
solver.set_initial_condition(U0)
u, t = solver.solve(t_vec,terminate)


S = u[:,0]
I = u[:,1]
R = u[:,2]

print "The maximum number of infected people is ", max(I)

plot_SIR(S,I,R,t)


"""
Ved sammenligning av plottene gitt av beta = 0.0001 og 0.0005 kommer det fram at det tar mye lengre tid før vi kommer til maksimum antall smittede med ca. 15  dager for beta = 0.0005 mot  ca. 120 dager for beta = 0.0001, altså har vi en raskere spredning av sykdommen. Dette gir mening siden beta er smitningsraten, som sier noe om hvor mange som blir smittet etter et møte mellom en infisert og en frisk person, så en høy beta vil gjøre at flere blir infisert raskere. VIdere ser vi at det er mange flere som blir smittet for beta = 0.0005 enn for beta = 0.001, med ca. 900 for beta = 0.0005 mot ca. 90 for beta = 0.0001. Dette er fordi sykdommen vil spre seg såpass sakta at den vil dø ut raskere.
"""


# Kjoreeksempel
# For beta = 0.0005
"""
maximum number of infected people is  897.87055421
"""
# For beta = 0.001
"""
The maximum number of infected people is  95.5347934588

"""
