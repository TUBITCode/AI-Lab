from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Gaussian Naïve Bayes classifier
model = GaussianNB()

# Train the model using the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the desired output
total_examples = X.shape[0]
training_examples = X_train.shape[0]
test_examples = X_test.shape[0]
print("Total number of examples are:", total_examples)
print("Out of these, training examples are:", training_examples)
print("Test examples are:", test_examples)
print("Accuracy of the model is:", accuracy)
