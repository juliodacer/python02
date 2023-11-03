# Filter crea una nueva lista
numbers = [1,2,3,4,5]
numbers_filter = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers_filter)
print(numbers)
