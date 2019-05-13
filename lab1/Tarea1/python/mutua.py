import sys

from utils.file_utils import read_file, read_maps, read_maps_frequencies
from utils.frequency_utils import count_characters, get_blocks, index_of_mutual_coincidence

if __name__== "__main__":

    text = read_file(sys.argv[1])
    maps = read_maps(sys.argv[2])
    frequencies = read_maps_frequencies(sys.argv[2])
    key_length = int(sys.argv[3])

    blocks = get_blocks(text, key_length)
    
    i = 0
    for block in blocks:

        i += 1
        print('Bloque ' + str(i))
        print('Simbolo  -  Indice')

        max_iomc = 0
        max_symbol = None
        counter = count_characters(block, maps)

        maps_length = len(maps)
        for j in range(0, maps_length):
            iomc = index_of_mutual_coincidence(maps, frequencies, counter, j, len(block))
            if iomc > max_iomc:
                max_iomc = iomc
                max_symbol = j
            print('   ' + str(j) + '     -      ' + str(iomc))

        print('Maximo en el simbolo: ' + str(maps[max_symbol]))
        print()