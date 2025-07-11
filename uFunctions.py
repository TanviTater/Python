import numpy as np
x = np.arange(4)
print("Original Array : ",x)
print("x        :",x)
print("x+5      :",np.add(x, 5))
print("x-5      :",np.subtract(x, 5))
print("x*2      :",np.multiply(x, 2))
print("x/2      :",np.divide(x, 2))
print("x**2     :",np.power(x, 2))
print("x//2     :",np.floor_divide(x, 2))
print("x%2      :",np.mod(x, 2))
print("-x       :",np.negative(x)) 
print('\n')
x2 = [-5,-4,-3,-2,-1,0]
print("x2       :",x2)
print("abs(x2)  :",np.abs(x2))
print("\n")
theta = np.linspace(0, np.pi, 3)
print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

print("\n")
x = [-1, 0, 1]
print("x         = ", x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))
print('\n')
x = [1, 2, 3]
print("x     =", x)
print("e^x   =", np.exp(x))
print("2^x   =", np.exp2(x))
print("3^x   =", np.power(3, x))
print('\n')
x = [1, 2, 4, 10]
print("x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))
print('\n')
x = [0, 0.001, 0.01, 0.1]
print("exp(x) - 1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))