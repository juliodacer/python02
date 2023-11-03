def multiply_numbers(numbers):
    return list(map(lambda number: number * 2, numbers))

array_numbers = [1, 2, -2, -3]
response = multiply_numbers(array_numbers)
print(response)