'''
Script para ejercicio 3
Correr python fermat_factorization.py N para encontrar la factorización N = pq
'''

# DEPENDENCIAS
# ------------------------------------------------
import sys
from sympy import sqrt, log, ceiling, Integer

# FUNCIONES AUXILIARES
# ------------------------------------------------

# Comprobar si 'n' es cuadrado perfecto
def is_square(n):
    return type(sqrt(n)) == Integer

# Obtener descomposición de 'n' = pq
def fermat_factor(n):

    # Optimización de la
    num_digits = int(log(n, 10).evalf() + 1)
    a = ceiling( sqrt(n).evalf(num_digits) )

    counter = 0
    while not is_square(a*a - n):
        a += 1
        counter += 1

        if a > n:
            return (0, 0, 0)

    b = sqrt(a*a - n)
    return(a+b, a-b, counter + 1)

# SECCIÓN PRINCIPAL
# ------------------------------------------------

# Leer parámetro y factorizarlo
N = int(sys.argv[1])
(p, q, counter) = fermat_factor(N)

# Si no se pudo descomponer
if p == 0:
    print("No se pudo encontrar la factorización de N = " + str(N) + " con este método.")
# Si se pudo descomponer
else:
    print("La factorización de N = " + str(N) + " devuelve los siguientes números:")
    print("-> p = " + str(p))
    print("-> q = " + str(q))
    print("Se necesitaron " + str(counter) + " iteraciones para encontrarlos.")

