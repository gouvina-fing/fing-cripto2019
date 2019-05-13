import sys

from utils.file_utils import read_file, read_maps
from utils.frequency_utils import count_characters, index_of_coincidence, get_blocks

if __name__== "__main__":

    text = read_file(sys.argv[1])
    maps = read_maps(sys.argv[2])
    key_length = int(sys.argv[3])

    blocks = get_blocks(text, key_length)
    i = 0
    for block in blocks:
        counter = count_characters(block, maps)
        ioc = index_of_coincidence(counter, len(blocks[0]))
        i += 1
        print('Indice de coincidencia en bloque ' + str(i) + ': ' + str(round(ioc, 6)))