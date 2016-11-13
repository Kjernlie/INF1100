# -*- coding: utf-8 -*-

class Line:
	def __init__(self, c0, c1):
		self.c0 = c0
		self.c1 = c1
	def __call__(self, x):
		y =  self.c0 + self.c1*x
		print "Line evaluated at ", x, " gives ", y
		return y
	def table(self, L, R, n):
		"""Return a table with n points for L <= x <= R."""
		s = ''
		import numpy as np
		for x in np.linspace(L, R, n):
			y = self(x)
			s += '%12g %12g\n' % (x, y)
		return s


class Parabola(Line):
	def __init__(self, c0, c1, c2):
		Line.__init__(self, c0, c1) 
		self.c2 = c2
	
	def __call__(self, x):
		y = Line.__call__(self, x) + self.c2*x**2
		print "Parabola evaluated at ", x, " gives ", y
		return y


class Cubic(Parabola):
	def __init__(self, c0, c1, c2, c3):
		Parabola.__init__(self, c0, c1, c2)
		self.c3 = c3
	
	def __call__(self, x):
		y = Parabola.__call__(self, x) + self.c3*x**3
		print "Cubic function evaluated at ", x, " gives ", y
		return y


class Poly4(Cubic):
	def __init__(self, c0, c1, c2, c3, c4):
		Cubic.__init__(self, c0, c1, c2, c3)
		self.c4 = c4

	def __call__(self, x):
		y = Cubic.__call__(self, x) + self.c4*x**4
		print "4th-order poly. evaluated at ", x, " gives ", y
		return y


c = Cubic(1, -2, 2, 1)
c1 = c(x=2.5)


p = Poly4(1,-2,2,1,2)
p1 = p(x=2.5)


# Kjoreeksempel
"""
Line evaluated at  2.5  gives  -4.0
Parabola evaluated at  2.5  gives  8.5
Cubic function evaluated at  2.5  gives  24.125
Line evaluated at  2.5  gives  -4.0
Parabola evaluated at  2.5  gives  8.5
Cubic function evaluated at  2.5  gives  24.125
4th-order poly. evaluated at  2.5  gives  102.25
"""
