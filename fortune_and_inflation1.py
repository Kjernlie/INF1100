def func(x0,p,q,I,N):
	xold = x0
	cold = p*q/(1e4)
	counter = 1
	x = []
	x.append(x0)
	while counter <= N:
		xnew = xold + (p/100.0)*xold - cold
		x.append(xnew)
		cnew = cold + I/(100.0)*xold
		xold = xnew
		cold = cnew
		counter += 1

	return x

import matplotlib.pyplot as plt
import seaborn as sns

x0 = 150
p = 5
N = 10
I = 0.5
q = 10
x = []
x = func(x0,p,q,I,N)


plt.plot(x)
plt.ylabel('Amount of money')
plt.xlabel('Year')
plt.show()






# Kjoreeksempel
"""

"""
