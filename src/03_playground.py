# Elimina elementos duplicados usando conjuntos

countries = {"MX", "COL", "ARG", "USA"}
north_am = {"USA", "CANADA"}
central_am = {"MX", "GT", "BZ"}
south_am = {"COL", "BZ", "ARG"}

new_set = set(countries | north_am | central_am | south_am)
print(new_set)