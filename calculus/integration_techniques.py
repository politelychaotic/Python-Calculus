# integration_techniques.py

import numpy as np
import scipy as sp
import sympy as sy
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import cumulative_trapezoid, trapezoid
from torch import positive

x = sy.symbols('x', real=True)
'''f = sy.sin(x)**3 * sy.exp(-5*x)
integrated = sy.integrate(f,x)
print(integrated)
print('\n')

a, b = sy.symbols('a b', real=True, positive=True)
f = sy.cos(b*x)*sy.exp(-a*x)
print(sy.integrate(f,x).simplify())
print('\n')

f = (1+sy.sqrt(x))**sy.Rational(1,3)/sy.sqrt(x) # sy.Rational(1,3) means to the 1/3 power
print(sy.integrate(f,x).simplify())
print('\n')

f = (sy.exp(x)/sy.sqrt(sy.exp(2*x)+9)) # for log
print(sy.integrate(f, (x, 0, sy.log(4))).evalf()) #x from zero to log4 base e
print('\n')

f = 16*sy.atan(x)/(1+x**2)
print(sy.integrate(f, (x, 0, sy.oo)))
print('\n')


# for definite integrals scipy

f = lambda x: np.exp(-np.sin(x))
print(quad(f, 1, 2))
print('\n')

a, b = 2, 3
f = lambda x: 1/((a-np.cos(x))**2 + (b-np.sin(x))**2)
print(quad(f, 0, 2*np.pi)) '''
# or to solve for many different values of a and b quickly

def f(x, a, b):
    return 1/((a-np.cos(x))**2 + (b-np.sin(x))**2)

'''a_array = np.arange(2,10,1) # 2 to 10 in steps of 1
b_array = np.arange(2,10,1)
integrals = [[a, b, quad(f, 0, 2*np.pi, args=(a,b))[0]] for a in a_array for b in b_array]
#print(integrals)
print(np.array(integrals).T[2])'''


# Using data (numeric)
x, y = np.loadtxt('energy_pulse_data.txt')
# suppose current is measured I(t)
# energy is proportional to integrated current

plt.plot(x,y)
plt.xlabel('Time [ns]')
plt.ylabel('Current [mA]')
plt.show()

integral = cumulative_trapezoid(y, x, initial=0) #estimate integral using trapezoid function
plt.plot(x, integral)
#print(integral)
plt.xlabel('Time [ns]')
plt.ylabel('Integrated Current [pC]')
plt.show()

