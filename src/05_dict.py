# dictionary comprehension
import random

dict = {}
for i in range(1, 11):
    dict[i] = i * 2
print(dict)

dict_v2 = {i: i * 2 for i in range(1, 11)}
print(dict_v2)

# example 2
countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
print(population)

countries_v2 = {country: random.randint(1, 100) for country in countries}
print(countries_v2)

# example 3
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

# output
'''
{
    'nico': 12,
    'zule': 56,
    'santi': 98
}
'''

# sol 1
names_dict = {}
counter = 0
for name in names:
    names_dict[name] = ages[counter]
    counter = counter + 1
print(names_dict)

# sol 2
names_dict_v2 = {}
for i in range(len(names)):
    names_dict_v2[names[i]] = ages[i]
print(names_dict_v2)

names_dict_v2 = {names[i]: ages[i] for i in range(len(names))}
print(names_dict_v2)

# sol 3
print(list(zip(names, ages)))
names_dict_v3 = {name: age for (name, age) in zip(names, ages)}
print(names_dict_v3)
