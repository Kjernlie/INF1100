from math import exp,pi
m = 0
s = 2
x = 1

def f(s,m,x):
    return ((2*pi)*s)**(-1/2)*exp(-0.5*((x-m)/s)**2)

print f(s,m,x)
