import sys
import operator

from utils.file_utils import read_file, read_maps
from utils.frequency_utils import count_trigrams, get_trigram_distances
from utils.math_utils import gcd

if __name__== "__main__":

    text = read_file(sys.argv[1])
    maps = read_maps(sys.argv[2])

    counter_trigrams = count_trigrams(text, maps)
    #sorted_trigrams_keys = sorted(counter_trigrams.items(), key=operator.itemgetter(0))
    sorted_trigrams_values = sorted(counter_trigrams.items(), key=operator.itemgetter(1), reverse=True)

    trigram_key, trigram_value = sorted_trigrams_values[0]
    first_found, trigram_distances = get_trigram_distances(text, maps, trigram_key)

    print('Trigrama más frecuente: ' + str(trigram_key) + ', ' + str(trigram_value) + ' ocurrencias')
    for distance in trigram_distances:
        print('Distancia de la ocurrencia n° ' + str(trigram_distances.index(distance) + 1) + ': ' + str(distance - first_found))
    print('El largo de la clave es: ' + str(gcd(trigram_distances)))