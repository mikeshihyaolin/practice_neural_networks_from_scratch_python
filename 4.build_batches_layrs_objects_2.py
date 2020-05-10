'''
Materials are from the tutorials:
Neural Networks from Scratch - P.4 Batches, Layers, and Objects
https://www.youtube.com/watch?v=TEWy9vZcxW4
'''
# Mike Lin
# Date: 2020-05-09

import numpy as np

np.random.seed(0)

'''input data'''
X = [[1.0, 2.0, 3.0, 2.5],
	 [2.0, 5.0, -1.0, 2.0],
	 [-1.5, 2.7, 3.3, -0.8]] #3x4


class Layer_Dense:

	def __init__(self, n_inputs, n_neurons):
		self.weights = 0.1* np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))

	def forward(self, inputs):
		self.ouput =np.dot(inputs, self.weights) + self.biases


layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
print(layer1.ouput)
layer2.forward(layer1.ouput)
print(layer2.ouput)
