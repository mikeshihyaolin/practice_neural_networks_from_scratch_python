'''
Materials are from the tutorials:
Neural Networks from Scratch - P.3 The Dot Product
https://www.youtube.com/watch?v=tMrbN67U9d4
'''
# Mike Lin
# Date: 2020-05-09

import numpy as np

'''input data'''
inputs = x = [1.0, 2.0, 3.0, 2.5] # 1x4
'''models with three neuros'''
weights = W = [[0.2, 0.8, -0.5, 1.0],
			   [0.5, -0.91, 0.26, -0.5],
			   [-0.26, -0.27, 0.17, 0.87]] #3*4
biases = b = [2.0, 3.0, 0.5]

layer_output = []

''' calculate with for loop '''
# for neuro_weight, neuro_bias in zip(W, b):
# 	neuro_output = 0
# 	for n_input, weight in zip(inputs, neuro_weight):
# 		neuro_output += n_input*weight
# 	neuro_output += neuro_bias
# 	layer_output.append(neuro_output)

# print(layer_output)

''' use numpy.dot"'''
output = np.dot(weights, inputs)+biases
print(output)
