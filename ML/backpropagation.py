import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the input dataset (AND gate inputs)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Define the output dataset (AND gate outputs)
y = np.array([[0], [0], [0], [1]])

# Seed the random number generator
np.random.seed(1)

# Initialize the weights with random values
weights = 2 * np.random.random((2, 1)) - 1

# Set the learning rate
learning_rate = 0.1

# Train the neural network
for i in range(10000):

    # Forward propagation
    layer = sigmoid(np.dot(X, weights))

    # Calculate the error
    error = y - layer

    # Backpropagation
    delta = error * sigmoid_derivative(layer)

    # Update the weights
    weights += learning_rate * np.dot(X.T, delta)

# Print the final weights
print("Final Weights:")
print(weights)

# Print the input values and corresponding predicted output
print("\nInput and Predicted Output (AND gate):")
for i in range(len(X)):
    input_values = X[i]
    predicted_output = layer[i][0]
    print(f"Input: {input_values}, Predicted Output: {predicted_output:.6f}")

