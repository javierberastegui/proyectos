def run():
    costo = float(input("¿Cuánto nos puesta el producto? "))
    multiplicador = 1.5
    margen = str(round(costo * multiplicador, 2))
    print(margen)

if __name__ == '__main__':
    run()