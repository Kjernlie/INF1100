from math import log, exp
class Decay:
	def __init__(self,a):
		self.a = a

	def __call__(self,u):
		return -self.a*u

	# Use rk4 to solve the ode
	def RungaKutta4(self,t0, tN, u0, N):
	        delta_t = (tN-t0) / float(N)
		u = u0
		t = t0
		u_list = []
		t_list = []
		u_list.append(u)
		t_list.append(t)
		for i in range(N):
			K1 = delta_t*self.__call__(u)
			K2 = delta_t*self.__call__(u+0.5*K1)
			K3 = delta_t*self.__call__(u+0.5*K2)
			K4 = delta_t*self.__call__(u+K3)
			u += 1./6*(K1+K2+K3+K4)
			t += delta_t
			u_list.append(u)
			t_list.append(t)
		return u_list, t_list



a = log(2)/5600
dec = Decay(a) 

t_final = 20000
t_start = 0  # adding zero afterwards
delta_t = 500
N = t_final/delta_t
u0 = 1

u, t = dec.RungaKutta4(t_start,t_final, u0, N)
u_exact_final = exp(-a*t_final)

print '%16s %16s' %('Computed value','Exact value')
print '%16.10f %16.10f' %(u[-1], u_exact_final)



# Kjoreeksempel
"""
  Computed value      Exact value
    0.1952760955     0.0841187620
"""
