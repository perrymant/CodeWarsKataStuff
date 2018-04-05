'''
https://www.codewars.com/kata/parabolas-standard-to-vertex-form/train/python
Parabolas: Standard to Vertex Form

a(x^2)+bx+c = a((x-h)^2) + k

getVertex(1,-10,16), [5,-9]

1(x**2)+-10*x+16

'''
from math import sqrt

a, b, c = 1,-10,16
def getVertex(a,b,c):
    d = b**2-4*a*c # discriminant
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    h = x1 - (x1 - x2)/2
    k = (h*a)**2 + (h*b) + c
    return [int(h), int(k)]


from math import sqrt

def getVertex(a,b,c):
    d = (b**2) - (4*a*c)
    x1 = (-b-sqrt(d))/(2*a)
    x2 = (-b+sqrt(d))/(2*a)
    h = x1 - (x1 - x2)/2 
    k = (h*a)**2 + (h*b) + c
    return [h, k]
