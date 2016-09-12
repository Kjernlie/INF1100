# Exercise 2.8 ball_table1

#import numpy as np
from tabulate import tabulate

g = 9.81 
v0 = 10
n = 9

#t = np.linspace(0,2*v0/g,n+1)
#y = np.zeros(n+1)
#
#def ym(t):
#    return v0*t-0.5*g*t**2
#y = ym(t)
#table = zip(t,y)
#print tabulate(table, headers = ["Time", "y"])


time = []
y2 = []
for i in range(n+1):
    time.append((2*v0/g)/(n)*i)
    y2.append(v0*time[i]-0.5*g*time[i]**2)

table2 = zip(time,y2)

print tabulate(table2, headers = ["Time", "y"])    
    
