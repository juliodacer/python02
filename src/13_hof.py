# Higher Order Function

def increment(x):
    return x + 1
increment_v2 = lambda x: x + 1
hoc_v2 = lambda x, func: x + func(x)
def hoc(x, func):
    return x + func(x)

result = hoc(20, increment)
# 20 + (20 + 1)
print(result)

