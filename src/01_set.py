# parecido a un diccionario
# set -> conjunto
# forma explicta de crear un set
set_countries = {'col', 'mex', 'bol', 'col'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 443, 23}
print(set_numbers)

set_types = {1, 'Hola', False, 12.12}
print(set_types)

# forma implicita
set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set('abc', 'cbv', 'as', 'abc')
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)

# convertir nuevamente a una lista los numeros unicos
unique_numbers = list(set_numbers)
print(unique_numbers)
