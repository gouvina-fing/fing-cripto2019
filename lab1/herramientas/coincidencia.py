import sys

from utils.file_utils import read_file, read_maps
from utils.frequency_utils import count_characters, index_of_coincidence

if __name__== "__main__":

    text = read_file(sys.argv[1])
    maps = read_maps(sys.argv[2])

    counter = count_characters(text, maps)
    ioc = index_of_coincidence(counter, len(text))

    print('Indice de Coincidencia: ' + str(round(ioc, 6)))