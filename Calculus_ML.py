import numpy as np

# Numerical Derivative

def derivative(f, x, h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)

f = lambda x: x**2 + 3*x

x_input = 2

print("\nDerivative of f(x)=x²+3x at x=2")
print(derivative(f, x_input))


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


# Jacobian Example
# F(x,y)= [x²+y , x+y²]

def jacobian(x,y):
    J=np.array([
        [2*x,1],
        [1,2*y]
    ])
    return J

print("\nJacobian at (1,2):")
print(jacobian(1,2))


# Taylor Approximation
# e^x ≈ 1+x+x²/2

x=.5

approx=1+x+(x**2)/2
actual=np.exp(x)

print("\nTaylor Approximation of e^0.5")
print("Approx:",approx)
print("Actual:",actual)


# Convex vs Non-Convex examples

convex=lambda x:x**2
non_convex=lambda x:x**4-3*x**2

x=1.5

print("\nConvex function x² at x=1.5:")
print(convex(x))

print("\nNon-convex function x⁴-3x² at x=1.5:")
print(non_convex(x))


# Backpropagation (Single Neuron)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# Input, weight, bias
x_input = 0.5
weight = 0.8
bias = 0.1

# Target
y_true = 1

# Forward pass
z = weight * x_input + bias
y_pred = sigmoid(z)

# Loss (Mean Squared Error)
loss = (y_pred - y_true)**2

# Backward pass (manual gradients)
dL_dy = 2 * (y_pred - y_true)
dy_dz = sigmoid_derivative(z)

dL_dz = dL_dy * dy_dz
dL_dw = dL_dz * x_input
dL_db = dL_dz * 1

print("\nBackpropagation (Single Neuron)")
print("Prediction:", y_pred)
print("Loss:", loss)
print("Gradient w:", dL_dw)
print("Gradient b:", dL_db)

# Parameter update
learning_rate = 0.1

weight = weight - learning_rate * dL_dw
bias = bias - learning_rate * dL_db

print("Updated weight:", weight)
print("Updated bias:", bias)

# Forward pass after update
new_z = weight * x_input + bias
new_y_pred = sigmoid(new_z)
new_loss = (new_y_pred - y_true)**2

print("New Loss after update:", new_loss)


# Batch Gradient Descent

X = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])  # y = 2x

weight = 0.0
lr = 0.01

for epoch in range(10):
    y_pred = weight * X
    loss = np.mean((y_pred - y)**2)

    grad = np.mean(2 * (y_pred - y) * X)

    weight -= lr * grad

    print(f"\nEpoch {epoch+1} | Loss: {loss:.4f} | weight: {weight:.4f}")


# Stochastic Gradient Descent

weight = 0.0
lr = 0.01

for epoch in range(5):
    for i in range(len(X)):
        y_pred = weight * X[i]
        grad = 2 * (y_pred - y[i]) * X[i]
        weight -= lr * grad

    print(f"\nEpoch {epoch+1} | weight: {weight:.4f}")


# Mini-Batch Gradient Descent

weight = 0.0
lr = 0.01
batch_size = 2

for epoch in range(5):

    for i in range(0, len(X), batch_size):

        X_batch = X[i:i+batch_size]
        y_batch = y[i:i+batch_size]

        y_pred = weight * X_batch

        grad = np.mean(2 * (y_pred - y_batch) * X_batch)

        weight -= lr * grad

    print(f"\nEpoch {epoch+1} | weight: {weight:.4f}")
    

# Gradient Descent with Momentum

weight = 0.0
lr = 0.01
momentum = 0.9
velocity = 0

for epoch in range(10):
    y_pred = weight * X
    grad = np.mean(2 * (y_pred - y) * X)

    velocity = momentum * velocity + lr * grad
    weight -= velocity

    print(f"\nEpoch {epoch+1} | weight: {weight:.4f}")


# Numerical Gradient Checking

def loss_fn(weight):
    return (weight * 2 - 4)**2

def analytical_grad(weight):
    return 2 * (weight * 2 - 4) * 2

def numerical_grad(weight, h=1e-5):
    return (loss_fn(weight + h) - loss_fn(weight - h)) / (2 * h)

weight = 1.0

print("\nGradient Checking")
print("Analytical Grad:", analytical_grad(weight))
print("Numerical Grad:", numerical_grad(weight))

difference = abs(analytical_grad(weight) - numerical_grad(weight))
print("Difference:", difference)
