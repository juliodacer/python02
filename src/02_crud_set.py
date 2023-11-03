set_countries = {'col', 'per', 'bol'}
size = len(set_countries)
print(size)

print('col' in set_countries)
print('mex' in set_countries)

# add
set_countries.add('mex')
print(set_countries)

# update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# remove
set_countries.remove('col')
print(set_countries)

# set_countries.remove('ardgfg') # si no existe da un error
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)
set_countries.clear() # eliminar todoo el conjunto
print(set_countries)
print(len(set_countries))