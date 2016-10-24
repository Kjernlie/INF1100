import numpy as np
from math import factorial, pi, sin
import matplotlib.pyplot as plt
import seaborn as sns

def S(x,n):
	s = 0
	for i in range(n+1):
		s += (-1.0)**i*(x**(2*i+1))/factorial(2*i+1)
	return s

NoS = 100
x = np.linspace(0,4*pi,NoS)
S1 = np.zeros(len(x))
S2 = np.zeros(len(x))
S3 = np.zeros(len(x))
S6 = np.zeros(len(x))
S12 = np.zeros(len(x))
for i in range(len(x)):
	S1[i] = S(x[i],1)
	S2[i] = S(x[i],2)
	S3[i] = S(x[i],3)
	S6[i] = S(x[i],6)
	S12[i] = S(x[i],12)

plt.plot(x,np.sin(x),x,S1,x,S2,x,S3,x,S6,x,S12)
plt.ylim([-1.5,1.5])
plt.legend(['sin(x)','S(x,1)','S(x,2)','S(x,3)','S(x,6)','S(x,12)'])
plt.show()

# Kjoreeksempel
"""

"""
