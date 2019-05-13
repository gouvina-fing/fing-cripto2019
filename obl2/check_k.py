'''
Script para ejercicio 2
Correr 'python check_k.py B' para encontrar un k que asegure que entre B y B+k hay un primo
'''

# DEPENDENCIAS
# ------------------------------------------------
import sys
import numpy as np
import sympy as sp
import matplotlib
import matplotlib.pyplot as plt

# FUNCIONES AUXILIARES
# ------------------------------------------------

def f(x):
	return x / np.log(x)

def g(x):
	return f(x) * (1 + (1/(2*np.log(x))))

def h(x):
	return f(x) * (1 + (3/(2*np.log(x))))

# SECCIÓN PRINCIPAL
# ------------------------------------------------

B = int(sys.argv[1])
k = int(sys.argv[2])
superiorB = h(B)

originalK = k
found = False

while not found:
	inferiorBk = g(B + k)
	difference = inferiorBk - superiorB
	found = difference >= 1
	k += 1

print('B = ' + str(B))
print('k = ' + str(k))
print('B + k = ' + str(B+k))
print('Cota superior = ' + str(superiorB))
print('Cota inferior = ' + str(inferiorBk))
print('Iteraciones = ' + str(k - originalK))