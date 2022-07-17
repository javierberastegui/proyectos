# Creamos nuestra lista de ejemplo 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Usamos map (multiplicando cada uno de los datos de mi lista por 5)
multiplicar = list(map(lambda x: x*2, lista))

print(multiplicar)