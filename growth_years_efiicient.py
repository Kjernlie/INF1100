x0 = 100                      # initial amount
p = 5                         # interest rate
N = 4                         # number of years

outfile = open('growth_rate.txt', 'w')


# Compute solution
xold = x0
counter = 1
while counter <= N:
	xnew = xold + (p/100.0)*xold
	xold = xnew
	outfile.write('The amount is %.6f' %xnew + '\n')
	counter += 1

outfile.close()


# Kjoreeksempel
"""

""" 
