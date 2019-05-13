import sys

from utils.file_utils import read_file, read_maps, read_key
from utils.frequency_utils import count_characters, get_blocks, index_of_mutual_coincidence

if __name__== "__main__":

    text = read_file(sys.argv[1])
    maps = read_maps(sys.argv[2])
    key = read_key(sys.argv[3])

    decryption = ''

    count = 0
    for char in text:
        count += 1

        if char in key:
            index = key.index(char)
            char_d = maps[index]
            decryption += char_d
        else:
            decryption += '(' + char + ')'

    print(decryption)