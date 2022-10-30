def run():
    costo = float(input("¿Cuánto nos puesta el producto? "))
    multiplicador = float(input("Introduce por lo que queremos que se multiplique nuestro margen: "))
    margen = str(round(costo * multiplicador, 2))
    print(margen)

if __name__ == '__main__':
    run()