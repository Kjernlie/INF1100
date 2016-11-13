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

t = 0
g_prime_exact = -exp(-t)

# Print error
print '%16s %16s' %('Backward1 error','Backward2 error')
for i in range(len(h)):
    bw1 = Backward1(g,h[i])
    error1 = abs(bw1(t) - g_prime_exact)
    bw2 = Backward2(g,h[i])
    error2 = abs(bw2(t) - g_prime_exact)
    print '%16.10f %16.10f' %(error1, error2)



# Kjoreeksempel
"""
 Backward1 error  Backward2 error
    0.7182818285     0.7579643925
    0.2974425414     0.1233967457
    0.1361016668     0.0252392079
    0.0651876245     0.0057264177
    0.0319113427     0.0013649392
    0.0157890400     0.0003332627
    0.0078533495     0.0000823409
    0.0039164424     0.0000204647
    0.0019556706     0.0000051012
    0.0009771986     0.0000012734
    0.0004884402     0.0000003181
    0.0002441804     0.0000000795
    0.0001220802     0.0000000199
    0.0000610376     0.0000000050
    0.0000305182     0.0000000012

"""
