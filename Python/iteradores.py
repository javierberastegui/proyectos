''' Lo primedo que vamos a hacer es crear un iterador '''

lista = [1, 2, 3, 4, 5]
iterador = iter(lista) # Nuestro iterador

''' Iterando el iterador '''

while True:
	try:
		elementos = next(iterador)
		print(elementos)
	except StopIteration:
		break
