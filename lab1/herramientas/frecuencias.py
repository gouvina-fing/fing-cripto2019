import sys
import operator

from utils.file_utils import read_file, read_maps
from utils.frequency_utils import count_characters, count_digrams, count_trigrams

if __name__== "__main__":

    text = read_file(sys.argv[1])
    maps = read_maps(sys.argv[2])

    counter_characters = count_characters(text, maps)
    counter_digrams = count_digrams(text, maps)
    counter_trigrams = count_trigrams(text, maps)

    total_characters = sum(counter_characters.values())
    total_digrams = sum(counter_digrams.values())
    total_trigrams = sum(counter_trigrams.values())

    print('Simbolo  -  Ocurrencias')
    for key in counter_characters:
        value = counter_characters[key]
        if value > 0:
            print('   ' + str(key) + '     -      ' + str(value))

    sorted_characters_values = sorted(counter_characters.items(), key=operator.itemgetter(1), reverse=True)
    print()
    print('Simbolo  -  Frecuencias')
    for key, value in sorted_characters_values:
        if value > 0:
            print('   ' + str(key) + '     -      ' + str(round(value / total_characters, 6)))

    sorted_digrams_keys = sorted(counter_digrams.items(), key=operator.itemgetter(0))
    print()
    print('Digrama  -  Ocurrencias')
    for key, value in sorted_digrams_keys:
        if value > 0:
            print('   ' + str(key) + '     -      ' + str(value))
    
    sorted_digrams_values = sorted(sorted_digrams_keys, key=operator.itemgetter(1), reverse=True)
    print()
    print('Digrama  -  Frecuencias')
    for key, value in sorted_digrams_values:
        if value > 0:
            print('   ' + str(key) + '     -      ' + str(round(value / total_digrams, 6)))

    sorted_trigrams_keys = sorted(counter_trigrams.items(), key=operator.itemgetter(0))
    print()
    print('Trigrama  -  Ocurrencias')
    for key, value in sorted_trigrams_keys:
        if value > 0:
            print('   ' + str(key) + '     -      ' + str(value))

    sorted_trigrams_values = sorted(sorted_trigrams_keys, key=operator.itemgetter(1), reverse=True)
    print()
    print('Trigrama  -  Frecuencias')
    for key, value in sorted_trigrams_values:
        if value > 0:
            print('   ' + str(key) + '     -      ' + str(round(value / total_trigrams, 6)))