import math

class SimpleDecisionTree:
    def __init__(self):
        self.tree = None

    def entropy(self, dataset):
        total_instances = len(dataset)
        label_counts = {}
        for row in dataset:
            label = row[-1]
            if label not in label_counts:
                label_counts[label] = 0
            label_counts[label] += 1

        entropy = 0
        for count in label_counts.values():
            prob = count / total_instances
            entropy -= prob * math.log2(prob) if prob > 0 else 0

        return entropy

    def information_gain(self, dataset, feature_index):
        total_instances = len(dataset)
        feature_values = {}
        for row in dataset:
            value = row[feature_index]
            if value not in feature_values:
                feature_values[value] = []
            feature_values[value].append(row)

        weighted_entropy = 0
        for value in feature_values.values():
            prob = len(value) / total_instances
            weighted_entropy += prob * self.entropy(value)

        return self.entropy(dataset) - weighted_entropy

    def best_split(self, dataset):
        best_feature = -1
        best_gain = -1

        for feature_index in range(len(dataset[0]) - 1):
            gain = self.information_gain(dataset, feature_index)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature_index

        return best_feature

    def fit(self, dataset):
        best_feature = self.best_split(dataset)
        self.tree = best_feature

    def predict(self, dataset):
        feature_index = self.tree
        predictions = []
        for row in dataset:
            predictions.append(row[feature_index])  # Predict based on the best feature
        return predictions


# Example usage
if __name__ == "__main__":
    dataset = [
        [1, 'Sunny', 'Hot', 'High', 'Weak', 'No'],
        [2, 'Sunny', 'Hot', 'High', 'Strong', 'No'],
        [3, 'Overcast', 'Hot', 'High', 'Weak', 'Yes'],
        [4, 'Rain', 'Mild', 'High', 'Weak', 'Yes'],
        [5, 'Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
        [6, 'Rain', 'Cool', 'Normal', 'Strong', 'No'],
        [7, 'Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
        [8, 'Sunny', 'Mild', 'High', 'Weak', 'No'],
        [9, 'Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
        [10, 'Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
        [11, 'Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
        [12, 'Overcast', 'Mild', 'High', 'Strong', 'Yes'],
        [13, 'Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
        [14, 'Rain', 'Mild', 'High', 'Strong', 'No']
    ]

    tree = SimpleDecisionTree()
    tree.fit([row[1:] for row in dataset])

    predictions = tree.predict([row[1:] for row in dataset])
    print("Predictions:", predictions)
