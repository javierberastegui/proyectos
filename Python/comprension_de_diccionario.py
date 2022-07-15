## Con comprensión de diccionario 

def run():

#	diccionario = {}
	
#	for i in range(1, 70):
#		if i % 2 != 0:
#			diccionario[i] = i**5	
			
    dic = {i: i**5 for i in range(1, 70) if i % 2 != 0}
    print(dic)


if __name__ == '__main__':
	run()