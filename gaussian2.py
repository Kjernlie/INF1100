import numpy as np

def gauss(x, m=0, s=1):
    f = 1/(np.sqrt(2*np.pi)*s)*np.exp(-0.5*((x-m)/s)**2)
    return f

m = 0
s = 1
n = 5
x = np.linspace(m-5*s,m+5*s,n)

print '      x    f(x)' 
for i in range(len(x)):
    f = gauss(x[i], m = 0, s = 1)
    print '%7.3f %7.3f' %(x[i], f)

# Kjoreeksempel
"""
Terminal > python gaussian2.py
      x    f(x)
 -5.000   0.000
 -2.500   0.018
  0.000   0.399
  2.500   0.018
  5.000   0.000
"""


