import numpy as np



x = eval(input('Enter value for x: '))
y = eval(input('Enter value for y: '))
z = eval(input('Enter value for z: '))

coefficient = 2

def gradient_vector(x, y, z):
    grad = [coefficient*x, coefficient*y, coefficient*z]
    return grad

gradient = gradient_vector(x,y,z)
print(len(gradient))


rho = eval(input('Enter value for Rho: '))
theta = eval(input('Enter value for Theta: '))
x_coord = np.sin(rho) * np.cos(theta)
y_coord = np.sin(rho) * np.sin(theta)
z_coord = np.cos(rho)

unit_vector = [x_coord, y_coord, z_coord]
print(gradient, unit_vector)

def np_dot(x,y, dim):
    dot_list = [[],[],[]]
    dot_product = 0
    for i in range(dim):
        dot_list[i] = x[i] *y[i] 
    for i in range(dim):
        dot_product += dot_list[i]
    return dot_product

dot_product = np_dot(gradient, unit_vector, len(gradient))
print(dot_product)



