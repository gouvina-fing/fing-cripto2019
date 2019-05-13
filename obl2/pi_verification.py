'''
Script para ejercicio 1
Correr 'python pi_verification.py x' para comprobar si pi(y) con 59 <= y <= x se encuentra acotado
'''

# DEPENDENCIAS
# ------------------------------------------------
import sys
import numpy as np
import sympy as sp

# FUNCIONES AUXILIARES
# ------------------------------------------------

def f(x):
	return x / np.log(x)

def g(x):
	return f(x) * (1 + (1/(2*np.log(x))))

def h(x):
	return f(x) * (1 + (3/(2*np.log(x))))

def pi(x):
	values = np.zeros(len(x))
	for index, val in enumerate(x):
		pi = sp.primepi(val)
		values[index] = pi
	return values

def division(x, func):
	return np.divide(func(x), f(x))

# SECCIÓN PRINCIPAL
# ------------------------------------------------

x = int(sys.argv[1])

counter = 59
closure = True
while closure and counter <= x:
	pi = sp.primepi(counter)
	closure = pi > g(counter) and pi < h(counter)
	counter += 1

if closure:
	print("La función pi(x) con x <= " + str(x) + " se encuentra acotada.")
else:
	print("La función pi(x) con x <= " + str(x) + " no se encuentra acotada para el valor " + str(counter - 1))

