F = 0
dF = 10

print '  F,      C,  C_hat'

while F <= 100:
    C = (5.0/9)*(F-32)
    C_hat = (F-30)/2.0

    print '%3d, %6.1f, %6.1f' %(F,C,C_hat)

    F += dF


# Kjoreeksempel
"""
Terminal > python f2c_approx_table.py
  F,      C,  C_hat
  0,  -17.8,  -15.0
 10,  -12.2,  -10.0
 20,   -6.7,   -5.0
 30,   -1.1,    0.0
 40,    4.4,    5.0
 50,   10.0,   10.0
 60,   15.6,   15.0
 70,   21.1,   20.0
 80,   26.7,   25.0
 90,   32.2,   30.0
100,   37.8,   35.0
"""
