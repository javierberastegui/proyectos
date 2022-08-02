def generador( ):
	
	''' Entendiendo los generadores '''
	
	print("Esto es un ejemplo, ")
	n = 0
	yield n
	
	print("es una forma más amigable, ")
	n = 1
	yield n
	
	print("simplifica nuestro trabajo.")
	n = 2
	yield n
	
g = generador( )
print(next(g))
print(next(g))
print(next(g))