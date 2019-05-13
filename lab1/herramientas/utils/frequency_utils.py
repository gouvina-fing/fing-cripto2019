# FRECUENCIAS
# Script con funciones auxiliares para el conteo de ocurrencias
# -------------------------------------------------------------

from utils.math_utils import arrangement

# FRECUENCIAS
# -------------------------------------------------------------

# Devuelve un diccionario con las ocurrencias en 'text' de cada 
# letra en 'maps', ignorando los caracteres que no están en 'maps' 
def count_characters(text, maps):

    counter =  {}
    
    for char in maps:
        counter[char] = 0

    for char in text:
        if char in maps:
            counter[char] += 1
            
    return counter

def count_digrams(text, maps):

    counter =  {}
    text_length = len(text)

    for i in range(0, text_length - 1):
        
        if text[i] not in maps or text[i+1] not in maps:
            continue

        digram = text[i] + text[i+1]

        if digram not in counter.keys():
            counter[digram] = 1
        else:
            counter[digram] += 1

    return counter

def count_trigrams(text, maps):

    counter =  {}
    text_length = len(text)

    for i in range(0, text_length - 2):
        
        if text[i] not in maps or text[i+1] not in maps or text[i+2] not in maps:
            continue

        trigram = text[i] + text[i+1] + text[i+2]

        if trigram not in counter.keys():
            counter[trigram] = 1
        else:
            counter[trigram] += 1

    return counter

# COINCIDENCIA
# -------------------------------------------------------------

def index_of_coincidence(counter, n):

    if n < 2:
        return -1

    total = arrangement(n, 2)
    reps = 0

    for key in counter:
        count = counter[key]
        if count > 1:
            reps += arrangement(count, 2)

    return reps / total

# COINCIDENCIA BLOQUES
# -------------------------------------------------------------

def get_blocks(text, length):

    columns = [text[i:i+length] for i in range(0, len(text), length)]
    rows = []

    for i in range(0, length):
        rows.append('')

    for column in columns:
        for i in range(0, len(column)):
            rows[i] += column[i]

    return rows

# KASISKI
# -------------------------------------------------------------
def get_trigram_distances(text, maps, trigram_key):

    trigram_distances = []
    text_length = len(text)

    for i in range(0, text_length - 2):
        
        if text[i] not in maps or text[i+1] not in maps or text[i+2] not in maps:
            continue

        trigram = text[i] + text[i+1] + text[i+2]

        if trigram == trigram_key:
            trigram_distances.append(i)

    return (trigram_distances[0], trigram_distances[1:])

# MUTUA
# -------------------------------------------------------------

def index_of_mutual_coincidence(maps, frequencies, counter, shifting, block_length):

    iomc = 0
    maps_length = len(maps)
    for i in range(0, maps_length):
        iomc += ( frequencies[i] * counter[maps[(i + shifting) % maps_length]]) / block_length

    return iomc