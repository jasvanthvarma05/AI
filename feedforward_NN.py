import random
import math

class SimpleFeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        
        # Initialize weights and biases with random values
        self.weights_input_hidden = [[random.random() for _ in range(hidden_size)] for _ in range(input_size)]
        self.weights_hidden_output = [random.random() for _ in range(hidden_size)]
        self.bias_hidden = [random.random() for _ in range(hidden_size)]
        self.bias_output = random.random()

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, X):
        self.hidden_input = [sum(X[i] * self.weights_input_hidden[i][j] for i in range(self.input_size)) + self.bias_hidden[j] for j in range(self.hidden_size)]
        self.hidden_output = [self.sigmoid(x) for x in self.hidden_input]
        
        self.final_input = sum(self.hidden_output[j] * self.weights_hidden_output[j] for j in range(self.hidden_size)) + self.bias_output
        self.final_output = self.sigmoid(self.final_input)
        
        return self.final_output

    def backward(self, X, y, output):
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)
        
        hidden_error = output_delta * sum(self.weights_hidden_output[j] for j in range(self.hidden_size))
        hidden_delta = [hidden_error * self.sigmoid_derivative(self.hidden_output[j]) for j in range(self.hidden_size)]
        
        # Update weights and biases
        for i in range(self.input_size):
            for j in range(self.hidden_size):
                self.weights_input_hidden[i][j] += self.learning_rate * X[i] * hidden_delta[j]
        
        for j in range(self.hidden_size):
            self.weights_hidden_output[j] += self.learning_rate * self.hidden_output[j] * output_delta
        
        for j in range(self.hidden_size):
            self.bias_hidden[j] += self.learning_rate * hidden_delta[j]
        
        self.bias_output += self.learning_rate * output_delta

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            for i in range(len(X)):
                output = self.forward(X[i])
                self.backward(X[i], y[i], output)
            
            if epoch % 1000 == 0:
                loss = sum((y[i] - self.forward(X[i])) ** 2 for i in range(len(X))) / len(X)
                print(f"Epoch {epoch}, Loss: {loss}")
                
    def predict(self, X):
        return [self.forward(x) for x in X]

if __name__ == "__main__":
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]  # XOR inputs
    y = [0, 1, 1, 0]  # XOR outputs
    
    model = SimpleFeedForwardNN(input_size=2, hidden_size=4, output_size=1)
    model.train(X, y, epochs=10000)
    
    predictions = model.predict(X)
    print("Predictions after training:", predictions)
