import numpy as np

# Numerical Derivative

def derivative(f, x, h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)

f = lambda x: x**2 + 3*x

x=2

print("\nDerivative of f(x)=x²+3x at x=2")
print(derivative(f,x))


# Partial Derivatives / Gradient
# f(x,y)=x² + y²
# grad=[2x,2y]

def gradient(x,y):
    dfdx=2*x
    dfdy=2*y
    return np.array([dfdx,dfdy])

print("\nGradient at (3,4):")
print(gradient(3,4))
