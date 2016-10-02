

# -------------------------------------------------------------------------------
# a)

def read(file):

    time = []

    count = 0
    for line in file:
        if count == 0:
            vel = line.split()
            v = float(vel[1])
        elif count > 1:
            time.append([float(i) for i in line.split()])

        count += 1

    flat_time = [item for sublist in time for item in sublist]           
 
    return v, flat_time

file = open("ball.dat")


# -----------------------------------------------------------------------------
# b)

from random import random, uniform

def maketest():
    outfile = open('test.dat', 'w')
    outfile.write('v0: 3.00' + '\n')
    outfile.write('t' + '\n')

    # Assuming 5 rows and between 2 and 6 elements in each
    data = []
    for i in range(5):
        length = int(uniform(2,7))
        data.append([random() for i in range(length)])
	
    for row in data:
	for column in row:
	    outfile.write('%.8f '%column)
	outfile.write('\n')
    outfile.close()


    file = open('test.dat')
    v, time = read(file)

    return v, time

print "\n"
print maketest()

# I don't understand what is ment by checking that the data is correct?


# ----------------------------------------------------------------------------
# c)


def y(t,v):
    g = 9.81
    y = v*t-0.5*g*t**2
    return y

def exercise_c(file):
    vel, time = read(file)
    time.sort()
    sol = []
    print('t      y   ')
    for i in range(len(time)):
	sol.append(y(time[i],vel))
        print('%.4f %.4f' %(time[i], sol[i]))
        

    return sol,time


print ('\n')	
exercise_c(file)    	

# --------------------------------------------------------------------------
# Kjoreeksempel


"""
(3.0, [0.06674555, 0.77012789, 0.65230592, 0.3494449, 0.28472889, 0.28956683, 0.87353882, 0.99027004, 0.97915886, 0.07304789, 0.23917642, 0.01796233, 0.83554902, 0.34716535, 0.32334624, 0.04337824, 0.92745996, 0.00593411, 0.12404843, 0.12268379, 0.80836904, 0.07407685, 0.78486616, 0.91938634])


t      y   
0.0420 0.1173
0.0519 0.1425
0.1026 0.2562
0.1117 0.2739
0.1559 0.3485
0.1738 0.3733
0.2094 0.4132
0.2134 0.4169
0.2139 0.4172
0.2700 0.4524
0.2807 0.4556
0.2958 0.4582
0.3465 0.4506
0.3500 0.4491
0.3681 0.4397
0.3730 0.4366
0.3933 0.4212
0.5062 0.2618
0.5280 0.2166
0.5301 0.2119
0.5768 0.0985
0.5798 0.0904

"""
