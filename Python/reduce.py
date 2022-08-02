#Importamos el modulo para poder trabajar con reduce 
from functools import reduce


# Creamos nuestra lista de ejemplo 
lista = [1, 2, 3, 4, 5]


todo_multiplicado = reduce(lambda x, y: x * y, lista)
print(todo_multiplicado)