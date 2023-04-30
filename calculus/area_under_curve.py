# area_under_curve.py
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
'''
to get this imports on your computer:
    1. open cmd and type:
        pip install sympy
        then,
        pip install numpy
        then,
        pip install matplotlib
'''

'''
Take the area under a curve and plot it
'''

def integrator(a,b,f, n):
    '''
    a = starting value
    b = stopping value
    n = number of rectangles
    f = predefined function in terms of some x
    '''
    width = (b-a)/n # takes the width based on (starting value - ending value)/number of rectangles <- accuracy restriction
    #print(width)
    #areas = [width*f(i) for i in range(1, n+1)] # calculates the area under the curve using the area of a rectangle and loops for total number of rectangle
    areas = [width*f(a+i*width) for i in range(1, n+1)]
    #print(areas)
    xs = sy.Symbol('xs') # sets up xs as a symbol for symbolic math (same as x, but if I use x here it will mess up everything else)
    exact = sy.integrate(f(xs), (xs, a, b)) # integrates (f(xs), (xs, starting value(a), ending value(b))
    print(f'Approximation with {n} rectangles is {sum(areas)}') #displays the sum of areas in the list areas[] created by iterating through each rectangle
    print(f'Exact area is {exact.evalf()}') #displays the area under the curve calculated by integration

    '''
    define x as all values between a(the starting value) - 0.5, 
    and the stopping value(b)+1.0, with the number of rectangles*100 being 
    the step size. (so inequality would be: a-0.5 < x < b+1) while keeping 
    x to be evenly spaced bewtween every point in this area. 
    the b+1 is there because linspace(start, end) includes all points except end,
    a-0.5 so that the graph starts a little before the starting point
    (so you can see it better)
    '''
    x = np.linspace(a-0.5, b+0.1, n*100)
    plt.figure(figsize=(15,7)) # sets the plot size
    plt.subplot(1,2,1) # subplot 1, this places lefthand plot for rectangle estimation
    plt.axhline(color = 'black') # sets axis (x,y) color to black
    for i in range(1, n+1): # start at 1, go to number of rectangles
        plt.vlines(a+width*i, 0, f(a+width*i)) # draws vertical lines for one side of the rectangles
        plt.vlines(a+width*(i-1), 0, f(a+width*i)) # draws vertical lines for other side of the rectangles
        plt.hlines(f(a+width*i), a+width*(i-1), a+width*i) # draws the top of rectangles
    plt.plot(x, f(x)) # plots (x, f(x)) when x is dependent on rectangle estimation, this is the lefthand plot
    plt.subplot(1, 2, 2) # sets up subplot 2, on the right
    plt.plot(x, f(x)) # uses same graph as before but filled in completely under the line to represent f(x) integrated
    plt.fill_between(x, f(x), where = [(x > a) and (x < b) for x in x]) # colors space below the curve
    plt.show() #displays the plot

def f(x): return x**2 # f(x)=x^4

def check_input(input): # this function just checks if input is a number and returns it as a number
    try:
        val = int(input)
        return val
    except ValueError:
        try:
            val = float(input)
            return val
        except ValueError:
            return False

def main():
    print('This program calculates the area under a curve\ngiven a starting point and ending point.')
    a = input('Enter where you want to start: ')
    b = input('Enter where you want to stop: ')
    n = input('How many rectangles should I use for my estimate? ')
    inlist = [a, b, n] # make inputs into a list so you can iterate through them
    #print(type(inlist))

    for i in range (len(inlist)):
        checker = check_input(inlist[i]) # tests inputs starting at index=0
        if checker == False:
            print('Please enter numbers only.')
            main() #calls main function again to start over
        else:
            inlist[i] = checker #if input is a number, then change data type to int or float respectively
    
    a = inlist[0] # set a as datatype it was detected to be
    b = inlist[1] # set b as datatypr it was detected to be
    n = int(inlist[2]) # n can only be an integer
        
    #print(type(a), type(b), type(n))
    integrator(a, b, f, n) # sends values to be integrated


if __name__ == "__main__":
    main()