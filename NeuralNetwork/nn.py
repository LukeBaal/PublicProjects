import numpy as np
import scipy.special

class NeuralNetwork:
	# Initialize neural network
	def __init__(self, inputnodes, hiddennodes, hiddenlayers, outputnodes, lr):
		self.inodes = inputnodes
		self.hlayers = [hiddennodes]*hiddenlayers

		# 1 hidden layer hard codded, given that the multiple
		# hidden layer runs are giving a much lower performace
		# with the current code
		self.hlayers = [hiddennodes]
		self.onodes = outputnodes

		# Learning rate
		self.lr  = lr

		# Make weight matrix for input layer and first hidden layer
		self.wih = np.random.normal(0.0, pow(self.hlayers[0], -0.5),
										(self.hlayers[0], self.inodes))

		# self.whh = []
		# # Make weight matrices for hidden layers if needed
		# if len(self.hlayers) > 1:
		# 	for i in range (len(self.hlayers)-1):
		# 		self.whh.append(np.random.normal(0.0, pow(self.hlayers[i+1], -0.5),
		# 										(self.hlayers[i+1], self.hlayers[i])))

		# Make weight matrix for last hidden layer and output layer
		self.who = np.random.normal(0.0, pow(self.onodes, -0.5),
										(self.onodes, self.hlayers[-1]))

		# Activation function is the sigmoid function (aka expit())
		self.activation_fcn = lambda x: scipy.special.expit(x)

		# Inverse activation function (for back query) is the inverse
		# of the sigmoid function (aka logit())
		self.inv_activation_fcn = lambda x: scipy.special.logit(x)

	# Train the neural network
	def train(self, inputs_list, targets_list):
		# Convert lists to 2d arrays
		inputs = np.array(inputs_list, ndmin=2).T
		targets = np.array(targets_list, ndmin=2).T

		# Calculate signals for hidden layer
		# Xh(hidden inputs)= Wh(hidden weights)*I(inputs)
		hidden_inputs = np.dot(self.wih, inputs)

		# Send Xh into activation function to get Oh(hidden outputs)
		hidden_outputs = []
		hidden_outputs.append(self.activation_fcn(hidden_inputs))

		# # Calculate signals for between hidden layers if needed
		# if self.whh != []:
		# 	for i in range(len(self.whh)):
		# 		hinputs = np.dot(self.whh[i], hidden_outputs[i])
		# 		hidden_outputs.append(self.activation_fcn(hinputs))

		# Calculate signals into final output layer (similar to above)
		final_inputs = np.dot(self.who, hidden_outputs[-1])
		final_outputs = self.activation_fcn(final_inputs)

		# Calulate the error (target-actual)
		output_errors = targets - final_outputs

		# Update the weights for the links between the hidden and output
		# layers
		self.who += self.lr * np.dot((output_errors * final_outputs *
					(1.0 - final_outputs)), np.transpose(hidden_outputs[-1]))

		# Last hidden layer error is the output_errors, split by weights,
		# recombines at hidden nodes
		hidden_errors = []
		hidden_errors.append(np.dot(self.who.T, output_errors))

		# # Update the weights for the links between the hidden layers if needed
		# index = 0
		# if self.whh != None:
		# 	for i in range(len(self.whh)-1, -1, -1):
		# 		#Tune weights
		# 		self.whh[i] += self.lr * np.dot((hidden_errors[index] * hidden_outputs[i+1] *
		# 					(1.0 - hidden_outputs[i+1])), np.transpose(hidden_outputs[i]))

		# 		# Calculate error for previous hidden layer
		# 		hidden_errors.append(np.dot(self.whh[i].T, hidden_errors[index]))
		# 		index += 1


		# Update the weights for the links between the input and hidden
		# layers
		self.wih += self.lr * np.dot((hidden_errors[-1] * hidden_outputs[0] *
					(1.0 - hidden_outputs[0])), np.transpose(inputs))



	#query the neural network
	def query(self, inputs_list):
		# Convert list to 2d array
		inputs = np.array(inputs_list, ndmin=2).T

		# Calcualte signals for hidden layer-----------
		# Xh(hidden inputs)= Wh(hidden weights)*I(inputs)
		hidden_inputs = np.dot(self.wih, inputs)

		# Send Xh into activation function to get Oh(hidden outputs)
		hidden_outputs = []
		hidden_outputs.append(self.activation_fcn(hidden_inputs))

		# # Calculate signals for between hidden layers if needed
		# if self.whh != []:
		# 	for i in range(len(self.whh)):
		# 		hinputs = np.dot(self.whh[i], hidden_outputs[i])
		# 		hidden_outputs.append(self.activation_fcn(hinputs))

		# Calculate signals into final output layer (similar to above)
		final_inputs = np.dot(self.who, hidden_outputs[-1])
		final_outputs = self.activation_fcn(final_inputs)

		return final_outputs

	# Give the network the output and it returns the input
	# Used to see what the network thinks each kind of output looks like
	def back_query(self, label_list):
		# Convert list to 2d array
		# print label_list
		final_outputs = np.array(label_list, ndmin=2).T
		# print final_outputs
		final_inputs = self.inv_activation_fcn(final_outputs)
		# print final_inputs
		# Calculate signals for hidden layer
		hidden_outputs = np.dot(self.who.T, final_inputs)

		# Scale to 0.01, 0.99
		hidden_outputs -= np.min(hidden_outputs)
		hidden_outputs /= np.max(hidden_outputs)
		hidden_outputs *= 0.98
		hidden_outputs += 0.01

		# Calculate the signal into hidden layer
		hidden_inputs = self.inv_activation_fcn(hidden_outputs)

		# Calculate signal output of the input layer
		inputs = np.dot(self.wih.T, hidden_inputs)

		# Scale to 0.01, 0.99
		inputs -= np.min(inputs)
		inputs /= np.max(inputs)
		inputs *= 0.98
		inputs += 0.01
		return inputs
