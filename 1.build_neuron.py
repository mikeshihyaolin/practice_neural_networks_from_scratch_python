'''
Materials are from the tutorials:
Neural Networks from Scratch - P.1 Intro and Neuron Code:
https://www.youtube.com/watch?v=Wo5dMEP_BbI
'''
# Mike Lin
# Date: 2020-05-09

import numpy as np

'''input data'''
inputs = x = [1.2, 5.1, 2.1]
'''models'''
weights = w = [3.1, 2.1, 8.7]
bias = b = 3

'''output = y = xw^{T}+b'''
output = y = x[0]*w[0]+ x[1]*w[1]+x[2]*w[2]+b
print("output: "+str(output))

# '''use for loop'''
# y = 0
# for i in range(len(x)):
# 	y += x[i]*w[i]
# y += b
# print("output: "+str(y))

