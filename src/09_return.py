# retornar multiples variables

def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola' # retorna 2 resultados

result, width, string = find_volume(length=10) # guardo los resultados
print(result)
print(width)
print(string)

