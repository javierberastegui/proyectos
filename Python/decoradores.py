from datetime import datetime

def tiempo_ejecucion(funcion):
	def envoltura(*args, **kwargs): # Empezamos el decorador
		tiempo_inicial = datetime.now( )
		funcion(*args, **kwargs)
		tiempo_final = datetime.now( )
		tiempo_total = tiempo_inicial - tiempo_final
		print("La ejecución ha tardado " + str(tiempo_total.total_seconds( )) + " segundos")
	return envoltura


@tiempo_ejecucion		
def operacion(x: int, y: int) -> int :
	multiplicador = x * y
	print(multiplicador)
	return operacion
	
@tiempo_ejecucion
def bucle( ):
	for i in range(1, 10):
		potencia = 2 ** i
		print(potencia)
		
@tiempo_ejecucion
def saludo(nombre = 'Martin'):
		print("Hola " + nombre)
		
		
operacion(132, 523)
saludo("javierberastegui.dev")
bucle( )