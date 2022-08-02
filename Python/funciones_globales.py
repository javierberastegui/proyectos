# Creamos funciones globales
x = 10

# Scope alcance local
def funcion():
	x = 20
	print(x)
	
	
def funcion2():
	x = 30
	print(x)

funcion()
funcion2()

print(x)