from numpy.lib.scimath import sqrt

def roots(a,b,c): 
    root1 = (-b + sqrt(b**2-4*a*c))/(2*a)
    root2 = (-b - sqrt(b**2-4*a*c))/(2*a)
    return root1,root2

def test_root_float(a,b,c):
    root1,root2 = roots(a,b,c)
    if isinstance(root1,float) == True and isinstance(root2,float) == True:
        a = ("The roots are not complex")
        return a

def test_root_complex(a,b,c):
    root1,root2 = roots(a,b,c)
    if isinstance(root1,complex) == True and isinstance(root2,complex) == True:
        a = ("The roots are complex")
        return a


# Real case
print roots(2,4,0), test_root_float(2,4,0), test_root_complex(2,4,0)

# Complex case
print roots(2,3,4), test_root_float(2,3,4), test_root_complex(2,3,4)


# Kjoreeksempel
"""
Terminal > python roots_quadratic.py
(0.0, -2.0) The roots are not complex None
((-0.75+1.1989578808281798j), (-0.75-1.1989578808281798j)) None The roots are complex
"""



          
