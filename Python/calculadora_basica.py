menu = '''
Bienvenidos a la calculadora interactiva de PYTHON

1- Refresco
2- Papas
3- Pizzas

elige la opción correcta: '''

opcion = int(input(menu))

if opcion == 1:
    costo = input('¿Cuanto te ha costado los refrescos?: ')
    costo = float(costo)
    valor_margen = 1.5
    margen = costo * valor_margen
    margen = round(margen, 2)
    margen = str(margen)

    print("El pvp es de " + margen + "€")

elif opcion == 2:
    costo = input('¿Cuanto te ha costado las papas?: ')
    costo = float(costo)
    valor_margen = 1.75
    margen = costo * valor_margen
    margen = round(margen, 2)
    margen = str(margen)

    print("El pvp es de " + margen + "€")

elif opcion == 3:
    costo = input('¿Cuanto te ha costado las pizzas?: ')
    costo = float(costo)
    valor_margen = 1.25
    margen = costo * valor_margen
    margen = round(margen, 2)
    margen = str(margen)

    print("El pvp es de " + margen + "€")

else:
    print('No hagas trampas, solo te he dado tres opciones. ')


