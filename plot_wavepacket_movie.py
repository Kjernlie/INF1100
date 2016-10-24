import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, glob, os

for name in glob.glob('tmp_*.pdf'):
	os.remove(name)

f = lambda x,t: np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))



# Create x,t and initial y-vector
x = np.linspace(-6,6,1001)
t_values = np.linspace(-1,1,61)
y = np.zeros(len(x))

plt.ion()
lines = plt.plot(x,y)
plt.axis([x[0],x[-1],-1,1])
plt.legend(['t=%4.2f' % t_values[0]])


counter = 0
for t in t_values:
	y = f(x,t)
	lines[0].set_ydata(y)
        plt.legend(['t=%4.2f' % t])
 	plt.draw()
	plt.savefig('tmp_%04d.png' % counter)
	counter += 1

os.system('convert -delay 6 tmp_*.png movie.gif')
os.system('gnome-open movie.gif')


# Kjoreeksempel
"""

"""
