from math import exp
import numpy as np

class Diff:
	def __init__(self, f, h=1E-5):
		self.f = f
		self.h = float(h)

class Backward1(Diff):
	def __call__(self, x):
		f, h = self.f, self.h
		return (f(x) - f(x-h))/h

class Backward2(Diff):
	def __call__(self, x):
		f, h = self.f, self.h
		return (f(x-2*h)-4*f(x-h)+3*f(x))/(2*h)


g = lambda t: exp(-t)

h = np.zeros(15)
for k in range(len(h)):
	h[k]= 2**(-k)


# Backward2
g_prime2 = np.zeros(len(h))
for i in range(len(h)):
	bw2 = Backward2(g, h[i])
	g_prime2[i] = bw2(x=0)

# Backward1
g_prime1 = np.zeros(len(h))
for i in range(len(h)):
	bw1 = Backward1(g, h[i])
	g_prime1[i] = bw1(x=0)



# Absolute error between Backward1 and Backward2
err = np.zeros(len(h))
err = np.abs(g_prime2-g_prime1)
print err


# Kjoreeksempel
"""
[  1.47624622e+00   4.20839287e-01   1.61340875e-01   7.09140422e-02
   3.32762818e-02   1.61223027e-02   7.93569042e-03   3.93690712e-03
   1.96077181e-03   9.78472024e-04   4.88758359e-04   2.44259868e-04
   1.22100119e-04   6.10426086e-05   3.05194371e-05]
"""
