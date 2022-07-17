# Creamos nuestra lista de ejemplo 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Usamos filter (filtramos numeros pares)
pares = list(filter(lambda par: par%2 == 0, lista))

print(pares)