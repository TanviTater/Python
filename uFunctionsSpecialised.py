from scipy import special
import numpy as np
# Gamma functions (generalized factorials) and related functions
x = [1, 5, 10]
print("gamma(x)     =", special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x, 2)   =", special.beta(x, 2))

# Error function (integral of Gaussian)
# its complement, and its inverse
x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x)  =", special.erf(x))
print("erfc(x) =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))

print('\n')
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)
y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)
x = np.arange(1, 6)
print("Add using Reduce : ", np.add.reduce(x))
print("Multiply using Reduce : ", np.multiply.reduce(x))
print("Add using Accumulate : ", np.add.accumulate(x))
print("Multiply using Accumulate : ", np.multiply.accumulate(x))
print("Add using Outer : ", np.add.outer(x, x))
print("Multiply using Outer : ", np.multiply.outer(x, x))