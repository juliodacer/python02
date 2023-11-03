def increment(x):
    return x + 1

increment_v2 = lambda x: x + 1

result = increment_v2(10)
print(result)

full_name = lambda name, last_name : f'Fullname es {name.title()} {last_name.title()}'
print((full_name('pepe', 'gavilan')))