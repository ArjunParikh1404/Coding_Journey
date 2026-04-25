import numpy as np

print("=== CALCULUS FOR MACHINE LEARNING ===")


# Numerical Derivative

def derivative(f, x, h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)

f = lambda x: x**2 + 3*x

x=2

print("\nDerivative of f(x)=x²+3x at x=2")
print(derivative(f,x))
