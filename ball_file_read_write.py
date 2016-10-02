

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

v, time = read(file)

print time

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


# ----------------------------------------------------------------------------
# c)
 
