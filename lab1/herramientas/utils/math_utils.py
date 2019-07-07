# CONTEO
# Script con funciones auxiliares para el conteo y aritmética
# -----------------------------------------------------------

import math
import numpy as np

# Devuelve un arreglo de m combinaciones tomadas de n
def arrangement(m, n):
	return math.factorial(m) / math.factorial(m-n)

# Devuelve el máximo común divisor para una lista de valores
def gcd(values):
	return np.gcd.reduce(values)