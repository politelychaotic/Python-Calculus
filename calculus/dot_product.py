import numpy as np

x = [5, 10]
y = [4, -7]

x1 = np.array([5, 10])
y1 = np.array([4, -7])

'''dot_product = np.dot(x,y)
dotty = x1 @ y1
print(dot_product, dotty)'''

def basic_np_dot(x,y):
    dot_product = np.dot(x, y)
    return dot_product


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

#product = A @ B
#print(product)

def np_arr_dot(x, y):
    dot_product = x @ y
    return dot_product

print(basic_np_dot(x, y))
print(np_arr_dot(A, B))

