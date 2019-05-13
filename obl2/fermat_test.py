'''
Script para ejercicio 2
Correr python fermat_test.py 1 N k para encontrar el primer número posiblemente primo mayor a N
Correr python fermat_test.py 2 N k para encontrar un testigo de fermat del primer compuesto siguiente a N
'''

# DEPENDENCIAS
# ------------------------------------------------
import sys
import math
import random

# FUNCIONES AUXILIARES
# ------------------------------------------------

# Implementación del test de fermat
def fermat_test(n, k, showWitness = False, showLiars = False):

    liarsCounter = 0
    
    if n == 2:
        return True

    if n % 2 == 0:
       return False

    if n % 10 == 5:
       return False

    for i in range(0, k):
       
        a = random.randint(1, n-1)
       
        if math.gcd(a, n) != 1:
            return False

        power = pow(a, n-1,n)

        if power % n != 1:
            if showWitness:
                print("El número " + str(a) + " es un testigo de Fermat para N = " + str(n))
            return False

        elif showLiars:
            liarsCounter += 1
            if liarsCounter <= 10:
                print("El número " + str(a) + " elevado a " + str(n-1) + " es congruente con 1 modulo " + str(n))
      
    return True

# SECCIÓN PRINCIPAL
# ------------------------------------------------

# Leer parámetros
op = int(sys.argv[1])
N = int(sys.argv[2])
k = int(sys.argv[3])

if op < 1 or op > 2:
    print('Opción incorrecta. Debe elegir un número entre 1 y 2.')
else:

    # Buscar primer número posiblemente primo
    if op == 1:

        originalN = N
        firstPossiblePrime = 0

        while firstPossiblePrime == 0:
            res = fermat_test(N, k)
            if res:
                firstPossiblePrime = N
                print('El primer posible primo para N = ' + str(originalN) + " es " + str(N))
                res = fermat_test(N, k, False, True)
            N += 1


    # Devolver testigo de fermat de primer número compuesto
    elif op == 2:

        originalN = N
        firstCompound = N + 1
        res = True

        while res:
            if firstCompound % 2 != 0:
                res = fermat_test(firstCompound, k, True)
            firstCompound += 1
