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


# Gradient Descent
# Minimize x²

def grad_descent(start, lr=.1, steps=20):
    x=start

    for i in range(steps):
        grad=2*x
        x=x-lr*grad
        print(f"Step {i+1}: x={x:.6f}")

    return x

print("\nGradient Descent minimizing x²:")
minimum=grad_descent(8)


# Chain Rule
# y=(3x+1)^2
# dy/dx = 2(3x+1)*3

def chain_rule(x):
    return 2*(3*x+1)*3

print("\nChain Rule derivative at x=2")
print(chain_rule(2))
