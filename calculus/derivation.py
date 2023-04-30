# derivation.py
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


'''def derive(y, n):
    y = n*x**(n-1)
    return y


x, y = sp.symbols('x y')
n = 45
c = 3

y = x**n+c
print(derive(y, n))'''


def integrate(N, a, b):
    def f(x): 
        return np.sin(x)

    value = 0
    value2 = 0
    for n in range(1, N+1):
        value += f(a+((n-(1/2))*((b-a)/N)))
    value2 = ((b-a)/N)*value
    return value2


print(integrate(N=10000, a=0, b=(2*np.pi)))

'''xs = sp.symbols('xs')

def g(xs): return sp.sin(xs)
a = 0
b = 2*sp.pi
exact = sp.integrate(g(xs), (xs, a, b))
print(exact)'''

def integrate_sin(a,b):
    return (-np.cos(b)+np.cos(a))

print(integrate_sin(a=0, b=2*np.pi))