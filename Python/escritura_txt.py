def read():
	numeros = [ ]
	with open("/storage/emulated/0/Documents/Archivos/numeros.txt", "r", encoding = "utf-8") as f:
		for lineas in f:
			numeros.append(int(lineas))
	print(numeros)
	

def write():
	nombres = ["Javi", "Ele", "Enri", "Adri", "Asa", "Julia", "Pablo"]
	with open("/storage/emulated/0/Documents/Archivos/nombres.txt", "w", encoding = "utf-8") as f: # Escribir  eliminando lo anterior 
	    for nombre in nombres:
		    f.write(nombre) #Write metodo para escribir 
		    f.write("\n") #Salto de linea
	

def run():
	write() # Aqui colocamos que funcion queremos pasar 
	
	
if __name__ == '__main__':
	run()