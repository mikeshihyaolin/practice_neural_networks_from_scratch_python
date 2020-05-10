'''
Materials are from the tutorials:
Neural Networks from Scratch - P.2 Coding a Layer
https://www.youtube.com/watch?v=lGLto9Xd7bU
'''
# Mike Lin
# Date: 2020-05-09

import numpy as np

'''input data'''
inputs = x = [1.0, 2.0, 3.0, 2.5]
'''models with three neuros'''
weights1 = w1 = [0.2, 0.8, -0.5, 1.0]
weights2 = w2 = [0.5, -0.91, 0.26, -0.5]
weights3 = w3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = b1 = 2.0
bias2 = b2 = 3.0
bias3 = b3 = 0.5


'''output = y = xw^{T}+b'''
output = y = [x[0]*w1[0]+ x[1]*w1[1]+x[2]*w1[2]+x[3]*w1[3]+b1,
			  x[0]*w2[0]+ x[1]*w2[1]+x[2]*w2[2]+x[3]*w2[3]+b2, 
			  x[0]*w3[0]+ x[1]*w3[1]+x[2]*w3[2]+x[3]*w3[3]+b3] 
print("output: "+str(output))


# # '''use for loop'''
# weights = W = [[0.2, 0.8, -0.5, 1.0],
#      [0.5, -0.91, 0.26, -0.5],
#      [-0.26, -0.27, 0.17, 0.87]]

# biases = b = [2.0, 3.0, 0.5]

# output = [0.0]*len(W)

# for i in range(len(W)):
# 	for j in range(len(W[0])):
# 		output[i] += W[i][j]*x[j]
# 	output[i] += b[i]

# print("output: "+str(output))



