# sets
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# UNION
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b) # | -> union operator

# INTERSECTION
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b) # & -> intersection operator

# DIFFERENCE
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b) # - -> difference operator

# SYMMETRIC DIFFERENCE
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b) # symmetric difference operator