# ARCHIVOS
# Script con funciones auxiliares para el manejo de archivos
# ----------------------------------------------------------

# Lee un archivo en la ruta 'route', devolviendolo como string
def read_file(route):
    with open (route, "r", encoding='latin-1') as file:
        text = file.read()
    return text

# Lee un mapa de un archivo en la ruta 'route, devolviendo como una lista
def read_maps(route):
    with open (route, "r", encoding='latin-1') as file:
        text = file.readline().rstrip()
    return text.split(',')

def read_maps_frequencies(route):
    with open (route, "r") as file:
        text = file.readline().rstrip()
        frequencies = file.readline().rstrip()
    frequencies = frequencies.split(',')
    return [float(i) for i in frequencies]

def read_key(route):
    with open (route, "r") as file:
        text = file.read()
    return text