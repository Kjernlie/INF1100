# ball_table3.py

#import numpy as np
from tabulate import tabulate

g = 9.81 
v0 = 10
n = 9


time = []
y2 = []
for i in range(n+1):
    time.append((2*v0/g)/(n)*i)
    y2.append(v0*time[i]-0.5*g*time[i]**2)


# a

ty1 = []
ty1.append(time) #ty1[0]
ty1.append(y2) #ty1[1]



for i in range(n+1):
    print '%.2f %.2f' %(ty1[0][i], ty1[1][i])


# b

ty2 = map(list, zip(*ty1))


for i in range(n+1):
    print '%.2f %.2f' %(ty2[i][0], ty2[i][1])

    
