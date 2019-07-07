'''
Script para ejercicio 1
Correr 'python pi_plots.py x' para generar distintas gráficas según x.
Las posibles gráficas son las siguientes:
-> x = 1: Graficar x/ln(x) y pi(x)
-> x = 2: Graficar x/ln(x) y las cotas
-> x = 3: Graficar pi(x) y las cotas
-> x = 4: Graficar x/ln(x), pi(x) y las cotas
-> x = 5: Graficar pi(x) / (x/ln(x)) y las cotas
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

param = int(sys.argv[1])

if param < 1 or param > 5:
	print('Opción incorrecta. Debe elegir un número entre 1 y 5.')

else:

	# Generar
	examples = np.arange(59, 10000, 1)

	# Funciones básicas
	fx = f(examples)
	gx = g(examples)
	hx = h(examples)
	pix = pi(examples)

	# Funciones divididas por x/ln(x)
	dpix = division(examples, pi)
	dgx = division(examples, g)
	dhx = division(examples, h)

	fig, ax = plt.subplots()

	# Casos
	if param == 1:
		ax.plot(examples, fx, '#396ab1', label="x/ln(x)")
		ax.plot(examples, pix, '#da7c30', label="pi(x)")

	elif param == 2:
		ax.plot(examples, fx, '#396ab1', label="x/ln(x)")
		ax.plot(examples, gx, '#3e9651', label="(x/ln(x)) * (1 + 1 / 2ln(x))")
		ax.plot(examples, hx, '#cc2551', label="(x/ln(x)) * (1 + 3 / 2ln(x))")

	elif param == 3:
		ax.plot(examples, pix, '#da7c30', label="pi(x)")
		ax.plot(examples, gx, '#3e9651', label="(x/ln(x)) * (1 + 1 / 2ln(x))")
		ax.plot(examples, hx, '#cc2551', label="(x/ln(x)) * (1 + 3 / 2ln(x))")

	elif param == 4:
		ax.plot(examples, fx, '#396ab1', label="x/ln(x)")
		ax.plot(examples, pix, '#da7c30', label="pi(x)")
		ax.plot(examples, gx, '#3e9651', label="(x/ln(x)) * (1 + 1 / 2ln(x))")
		ax.plot(examples, hx, '#cc2551', label="(x/ln(x)) * (1 + 3 / 2ln(x))")

	elif param == 5:
		ax.plot(examples, dpix, label="pi(x) / (x/ln(x))")
		ax.plot(examples, dgx, label="1 + 1 / 2ln(x)")
		ax.plot(examples, dhx, label="1 + 3 / 2ln(x)")

	ax.legend()
	plt.show()
