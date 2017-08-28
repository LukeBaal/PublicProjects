from nn import NeuralNetwork
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#Declare # of nodes for the neural network
input_nodes = 4
hidden_nodes = 500
hidden_layers = 1
output_nodes = 15
learning_rate  = 0.3
max_value = 290.677

n = NeuralNetwork(input_nodes,hidden_nodes, hidden_layers, output_nodes, learning_rate)

# Open and read train data
train_file = open("pentagon_train_data.csv", 'r')
train_data = train_file.readlines()
train_file.close()

# Scale each value to be between 0.01-0.99
# Then train the network using training data
for entry in train_data:
    vals = entry.split(',')

    inputs = (np.asfarray(vals[1:]) / max_value * 0.99) + 0.01

    targets = np.zeros(output_nodes) + 0.01

    index = int(vals[0]) - 1
    targets[index] = 0.99
    n.train(inputs, targets)

# Open and read test data
test_file = open("pentagon_test_data.csv", 'r')
test_data = test_file.readlines()
test_file.close()

scorecard = []

for entry in test_data:
    vals = entry.split(',')

    correct_label = int(vals[0])
    inputs = (np.asfarray(vals[1:]) / max_value * 0.99) + 0.01

    outputs = n.query(inputs)

    label = np.argmax(outputs)

    if label == correct_label:
        scorecard.append(1)
    else:
        scorecard.append(0)

# Calculate the accuracy of the neural network
scorecard_array = np.asfarray(scorecard)
accuracy = float(scorecard_array.sum()) / float(scorecard_array.size) * 100
print "performance = ", str(accuracy) + "%"


# for i in range(output_nodes):
targets = np.zeros(output_nodes) + 0.01
targets[0] = 0.99

output = n.back_query(targets)

output -= 0.01
output /= 0.99
output *= max_value
angle_sum = 0
for item in output[:4]:
    angle_sum += item

print output, angle_sum 

