def capicuo(x: int) -> bool:
	return x == x[::-1]

def run():
	x = input('Escribe un numero: ')
	x = x.replace(" ", "")
	print(capicuo(x))


if __name__ == "__main__":
	run()