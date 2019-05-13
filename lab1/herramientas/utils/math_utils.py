# CONTEO
# Script con funciones auxiliares para el conteo y aritmética
# -----------------------------------------------------------

import math
import numpy as np

# 
def arrangement(n, m):
	return math.factorial(n) / math.factorial(n-m)

# 
def combination(n, r):
	return math.factorial(n - r) * math.factorial(r)

def gcd(values):
	return np.gcd.reduce(values)