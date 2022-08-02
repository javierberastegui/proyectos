import time 

''' Mejorando nuestro script fibonacci '''

def g_fibo( ):
	n1 = 0
	n2 = 1
	contador = 0
	while True: # bucle infinito
		if contador == 0:
			contador += 1
			yield n1
		elif contador == 1:
			contador += 1
			yield n2
		else:
			aux = n1 + n2
			n1, n2 = n2, aux
			contador += 1
			yield aux

''' Instanciamos el generador '''
if __name__ == '__main__':
		fibonacci = g_fibo( )
		for elementos in fibonacci:
			print(elementos)
			time.sleep(0.25)