import numpy as np

def triangle_area(vertices):
    A = 0.5*(vertices[1][0]*vertices[2][1]-vertices[2][0]*vertices[1][1]-vertices[0][0]*vertices[2][1] + vertices[2][0]*vertices[0][1]+vertices[0][0]*vertices[1][1]-vertices[1][0]*vertices[0][1])

    return A

def test_triangle_area():

    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1, v2, v3]
    expected = 1.0
    computed = triangle_area(vertices)
    tol = 1E-14
    success = np.absolute(expected - computed) < tol
    msg = 'computed area=%g != %g (expected)' %(computed, expected) 
    assert success, msg

a = []
a = test_triangle_area()
print a



# Kjoreeksempel
"""
Terminal > python area_triangle.py
None
"""

    

