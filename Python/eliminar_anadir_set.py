''' Creamos la lista '''
lista = [1, 2, 2, 2, 3, 8, 11, 3, 4, 5] # Por ejemplo

''' Creamos el set ''' 
set = set(lista)
print("Asi transformamos a un set ->", set)

''' Añadimos un elemento '''
set.add(7)
print(set)

''' Añadimos un conjunto (una lista y un set) '''
set.update([7, 9, 10, 24], {True, False})
print(set)

''' Eliminando dato con discard '''
set.remove(True)
print(set)

''' Eliminando con discard '''
set.discard(False)
print(set)

''' Borrar elementos aleatorios (no tiene mucho sentido)'''
set.pop()
print(set)

''' Eliminar todos los datos del set '''
set.clear
print(set)