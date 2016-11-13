from math import sin,cos,pi,exp
import matplotlib.pyplot as plt

# f: function to solve du/dt=f(u,t)
# t0: initial value of t
# tN: final value of t
# u0: initial value of u
# N: number of steps
def RungaKutta2(f, t0, tN, u0, N):
	delta_t = (tN-t0) / float(N)
	u = u0
	t = t0
	u_list = []
	t_list = []
	u_list.append(u)
	t_list.append(t)
	for i in range(N):
		K1 = delta_t*f(u,t)
		K2 = delta_t*f(u+0.5*K1,t+0.5*delta_t)
		u += K2
		t += delta_t
		u_list.append(u)
		t_list.append(t)
	return u_list, t_list


def test_rk2(N):
	expected = 267.2458278
	u, t = RungaKutta2(lambda u,t: u + sin(t),0,2*pi,0,N)
	computed = u[-1]
	tol = 1e-6
	success = abs(expected-computed) < tol
	msg = 'not working'
	assert success, msg


f = lambda u,t: u + sin(t)
exact_func = lambda t: 0.5*(exp(t)-sin(t)-cos(t))

u, t = RungaKutta2(f,0,2*pi,0,100)

u_exact = []
for i in range(len(t)):
	u_exact.append(exact_func(t[i]))

plt.plot(t,u,t,u_exact)
plt.show()


test_rk2(200000)
#test_rk2(100000)


# -------------------------------------------------------
# Kjoreksempel 

# with test_rk2(200000)
"""

"""


		
# with test_rk2(100000)
"""
traceback (most recent call last):
  File "RungaKutta2_func.py", line 51, in <module>
    test_rk2(1000000)
  File "RungaKutta2_func.py", line 35, in test_rk2
    assert success, msg
AssertionError: not working

"""	
