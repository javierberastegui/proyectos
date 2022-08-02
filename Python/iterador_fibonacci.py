import time

class FiboIter( ):
	
	''' Reproducir todos y cada uno de los números de la cadena de fibonacci '''
	
	def __iter__(self):
		self.n1 = 0
		self.n2 = 1
		self.contador = 0
		return self
		
	def __next__(self):
		if self.contador == 0:
			self.contador += 1
			return self.n1
		elif self.contador == 1:
			self.contador += 1
			return self.n2
		else:
			self.aux = self.n1 + self.n2 
			self.n1, self.n2 = self.n2, self.aux 
			self.contador += 1
			return self.aux 
			
if __name__ == '__main__':
	fibonacci = FiboIter( ) # Instanciar al iterador 
	for elemento in fibonacci:
		print(elemento)
		time.sleep(0.25)