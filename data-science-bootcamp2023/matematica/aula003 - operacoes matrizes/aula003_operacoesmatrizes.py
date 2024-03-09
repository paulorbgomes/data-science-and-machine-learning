# -*- coding: utf-8 -*-
"""aula003_operacoesMatrizes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YHhkJXnMyUABhcYFi3tr7UPXUyY8DpRf
"""

# Bibliotecas
import numpy as np

# Soma de Matrizes
m1 = np.array([[5, 12, 6], [-3, 0, 14]])
m2 = np.array([[9, 8, 7], [1, 3, -5]])
m1 + m2

# Subtração de Matrizes
m1 - m2

# Soma e Subtração de Vetores
v1 = np.array([1, 2, 3])
v2 = np.array([10, 20, 30])
v1 + v2
v1 - v2

# Transposição
x = np.array([1, 2, 3])
print(x.shape)
xT = x.reshape(1,3)
print(xT.shape)
xTT = xT.reshape(3,1)
print(xTT.shape)

print(x)
print(xT)
print(xTT)

print("Matriz A")
A = np.array([[5, 12, 6], [-3, 0, 14]])
print(A)
print(A.T)

print("Matriz B")
B = np.array([[5, 3], [-2, 4]])
print(B)
print(B.T)

# Produto Escalar
print("Operação com Escalares")
s1 = np.array(6)
s2 = np.array(5)
s1 * s2
print(np.dot(s1, s2))

print("Operação com Vetores")
v1 = np.array([2, 8, -4])
v2 = np.array([1, -7, 3])
v1 * v2          # equivalente ao produto de Hadamard
np.dot(v1, v2)   # produto interno

u = np.array([0, 2, 5, 8])
v = np.array([20, 3, 4, -1])
np.dot(u, v)
np.dot(2, v)

# Produto Entre Matrizes
'''
A = np.array([[5, 12, 6], [-3, 0, 14]])
#np.dot(3, A)
B = np.array([[1, 2], [3, 4], [5, 6]])
print(A.shape, B.shape)
np.dot(A, B)
'''

'''
A = np.array([2, 8, -4])
B = np.array([1, -7, 3])
np.dot(A.reshape(1,3), B)
'''

A = np.array([[5, 12, 6], [-3, 0, 14]])
print(A.shape)
B = np.array([[2, -1], [8, 0], [3, 0]])
print(B.shape)
np.dot(A, B)

print("Outro exemplo ...")
A = np.array([[-12, 5, -5, 1, 6], [6, -2, 0, 0, -3], [10, 2, 0, 8, 0], [9, -4, 8, 3, -6]])
B = np.array([[6, -1], [8, -4], [2, -2], [7, 4], [-6, -9]])
print(A.shape, B.shape)
np.dot(A, B)