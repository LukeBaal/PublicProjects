import numpy as np
import scipy.special

class NeuralNetwork:
	# Initialize neural network
	def __init__(self, inputnodes, hiddennodes, outputnodes, lr):
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes
		
		# Learning rate
		self.lr  = lr
		
		# Link weight matrices, wih and who
		self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5),
										(self.hnodes, self.inodes))
		self.who = np.random.normal(0.0, pow(self.onodes, -0.5), 
										(self.onodes, self.hnodes))
										
	# Activation function is the sigmoid function (aka expit())
		self.activation_fcn = lambda x: scipy.special.expit(x)


	# Train the neural network
	def train(self, inputs_list, targets_list):
		# Convert lists to 2d arrays
		inputs = np.array(inputs_list, ndmin=2).T
		targets = np.array(targets_list, ndmin=2).T

		# Calculate signals for hidden layer
		# Xh(hidden inputs)= Wh(hidden weights)*I(inputs)
		hidden_inputs = np.dot(self.wih, inputs)
		
		# Send Xh into activation function to get Oh(hidden outputs)
		hidden_outputs = self.activation_fcn(hidden_inputs)
		
		# Calculate signals into final output layer (similar to above)
		final_inputs = np.dot(self.who, hidden_outputs)
		final_outputs = self.activation_fcn(final_inputs)
		
		# Calulate the error (target-actual)
		output_errors = targets - final_outputs
		
		# Hidden layer error is the output_errors, split by weights,
		# recombines at hideen nodes
		hidden_errors = np.dot(self.who.T, output_errors)
		
		# Update the weights for the links between the hidden and output
		# layers
		self.who += self.lr * np.dot((output_errors * final_outputs * 
					(1.0 - final_outputs)), np.transpose(hidden_outputs))
					
		# Update the weights for the links between the input and hidden
		# layers
		self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * 
					(1.0 - hidden_outputs)), np.transpose(inputs))
		
	
	
	#query the neural network
	def query(self, inputs_list):
		# Convert list to 2d array
		inputs = np.array(inputs_list, ndmin=2).T
		
		# Calcualte signals for hidden layer-----------
		# Xh(hidden inputs)= Wh(hidden weights)*I(inputs)
		hidden_inputs = np.dot(self.wih, inputs)
		
		# Send Xh into activation function to get Oh(hidden outputs)
		hidden_outputs = self.activation_fcn(hidden_inputs)
		
		
		# Calculate signals into final output layer (similar to above)
		final_inputs = np.dot(self.who, hidden_outputs)
		final_outputs = self.activation_fcn(final_inputs)

		return final_outputs




	
