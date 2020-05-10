'''
Materials are from the tutorials:
Neural Networks from Scratch - P.4 Batches, Layers, and Objects
https://www.youtube.com/watch?v=TEWy9vZcxW4
'''
# Mike Lin
# Date: 2020-05-09

import numpy as np

'''input data'''
inputs = X = [[1.0, 2.0, 3.0, 2.5],
			  [2.0, 5.0, -1.0, 2.0],
			  [-1.5, 2.7, 3.3, -0.8]] #3x4
# '''models with three neuros'''
# weights = W = [[0.2, 0.8, -0.5, 1.0],
# 			   [0.5, -0.91, 0.26, -0.5],
# 			   [-0.26, -0.27, 0.17, 0.87]] #3*4
# biases = b = [2.0, 3.0, 0.5]

# # XW^{T}+b
# output = np.dot(inputs, np.array(weights).T)+biases
# print(output)

 # ---------------------------- #

# multi-layers
# layer 1
weight1 = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
		   [-0.26, -0.27, 0.17, 0.87]] #3*4
biases1 = [2.0, 3.0, 0.5]
# layer2
weight2 = [[0.1, 0.14, 0.5],
           [-0.5,0.12, -0.33],
		   [-0.44, 0.73, -0.13]] #3*3
biases2   = [-1, 2, -0.5]

layer1_output = np.dot(inputs, np.array(weight1).T)+biases1 # 3x4 x 4x3
layer2_output = np.dot(layer1_output, np.array(weight2).T)+biases2 # 3x3 x 3x3
print(layer2_output)


