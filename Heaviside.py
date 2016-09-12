def H(x):
    if x < 0.0:
        H = 0
    else:
        H = 1
    return H

def test_H():
    print 'H(-10) should be 0, and is %d' %H(-10)
    print 'H(-10**(-15)) should be 0, and is %d' %H(-10**(-15))
    print 'H(0) should be 1, and is %d' %H(0)
    print 'H(10**(-15)) should be 1, and is %d' %H(10**(-15))
    print 'H(10) should be 1, and is %d' %H(10)

test_H()



# Kjoreeksempel
"""
Terminal > python Heaviside.py
H(-10) should be 0, and is 0
H(-10**(-15)) should be 0, and is 0
H(0) should be 1, and is 1
H(10**(-15)) should be 1, and is 1
H(10) should be 1, and is 1
"""
