from nn import NeuralNetwork
import numpy
import matplotlib.pyplot as plt

#Declare # of nodes for the neural network
input_nodes = 784
hidden_nodes = 100
output_nodes = 10
learning_rate  = 0.3

n = NeuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)

training_data_file = open("mnist_train.csv", 'r')
training_data = training_data_file.readlines()
training_data_file.close()

# Train the network
for record in training_data:
	#Split the string into a list and scale/shift values
	all_values =record.split(',')
	inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01

	targets = numpy.zeros(output_nodes) + 0.01
	targets[int(all_values[0])] = 0.99
	n.train(inputs, targets)


# Load test data into a list
test_data_file = open("mnist_test.csv", 'r')
test_data = test_data_file.readlines()
test_data_file.close()

scorecard  = []
# Test the neural network
for record in test_data:
	all_values = record.split(',')
	
	# Correct answer is first value
	correct_label = int(all_values[0])
	#print correct_label, "correct label"
	 
	# Scale/shift the data 
	inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
	
	# Query the network
	outputs = n.query(inputs)
	
	# The index of the highest value corresponds to the label
	# ie the networks guess of which digit it is
	label = numpy.argmax(outputs)
	#print label, "network's answer"
	
	# Append correct or inccorect to the list
	if label == correct_label:
		scorecard.append(1)
	else:
		scorecard.append(0)

# Calculate the accuracy of the neural network
scorecard_array = numpy.asarray(scorecard)
accuracy  = float(scorecard_array.sum()) / float(scorecard_array.size) * 100
print "performance = ", accuracy
