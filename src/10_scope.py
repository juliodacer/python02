#scope -> alcance
price = 100 # global

def increment():
    price = 200
    return price + 10

print(price)
print(increment())