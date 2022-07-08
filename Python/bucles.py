def run(): # Invocamos la función
    LIMITE = 80000

    exponente = 0 
    base = 2**exponente
    while base < LIMITE: # Mientras que base sea menor al límite 
        print('2 elevado a ' + str(exponente) + ' es igual a: ' + str(base))
## Quitar bucle infinito xD        
        exponente = exponente + 1 
        base = 2**exponente


if __name__ == '__main__':
    run()