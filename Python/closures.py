''' ¿Cómo utilizar los closures en PYTHON? '''

def valores( ):
	x = 10
	y = 5
	
	
	def operacion( ):
		multiplicador = x * y
		print(multiplicador)
	
	
	return operacion # Retornamos operacion


# Creamos variable deseada 
resultado = valores( )
resultado( )

''' Eliminando la función superior valores '''
del(valores)
''' Imprimiendo resultado'''
resultado( )