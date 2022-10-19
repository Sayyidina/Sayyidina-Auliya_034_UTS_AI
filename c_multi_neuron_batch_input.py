# -*- coding: utf-8 -*-
"""c.multi neuron batch input.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18KNAKrMB_KnmjuDd9LNH_LrmXgtjGIBK
"""

#Sayyidina Auliya
#21091397034

#inisialisasi library
import numpy as np

#input layer feature 10
#per batch 6 input
inputs = [
    [0.4,0.8,1.2,1.5,-0.7,4.4,1.8,2.1,1.3,2.4],
    [3.8,-1.0,-1.6,2.7,3.2,3.5,-1.9,-4.2,1.4,-0.9],
    [1.7,2.5,3.4,2.8,2.0,3.6,3.9,3.1,2.3,2.9],
    [3.3,3.7,2.6,4.1,3.0,1.1,2.2,0.81,-1.99,3.74],
    [0.2,-0.27,3.8,1.4,6.667,5.1,0.73,0.11,2.78,4.0],
    [-0.8,-0.9,-0.10,3.7,2.3,4,8.1,3.33,0.65,4.6]
]

weights = [
    [2.5,1.3,-1.3,2.1,0.1,3.2,-2.1,1.1,0.34,-0.77],
    [0.3,3.6,-6.0,2.7,1.31,3.9,0.76,9.0,4.9,2.5],
    [0.81,1.5,-1.5,5.8,9.2,1.6,0.71,-0.5,2,1.0],
    [0.2,0.57,5.5,9.8,9.01,6.6,0.85,7.3,5.90,4.1],
    [7.1,3.29,4,6,9.9,0.27,1.3,-1.7,-0.2,1.7]
]

#neuron 5
biases = [4,5,0.3,1.7,0.2]

#menampilkan keluaran
outputs = np.dot(inputs, np.array(weights). T)+ biases
print(outputs)