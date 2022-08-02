class EventNumbers:
	
	''' Clase que implementa un iterador con los números pares hasta un máximo '''
	
	def __unit__( self, max = None ):
		self.max = max 
		
	def __iter__(self):
		self.num = 0
		return self
		
	def __next__(self):
		if not self.max or self.num <= self.max:
			resultado = self.num
			self.num += 2
			return resultado
		else:
			raise StopIteration