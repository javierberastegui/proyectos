def opciones(mensaje, valor_margen):
    costo = input(mensaje) 
    costo = float(costo) 
    margen = costo * valor_margen 
    margen = round(margen, 2)
    margen = str(margen) 
    print("El PVP es de " + margen + "€")

menu = """
Bienvenida a la calculadora interactiva de PYTHON 😊💸

1 - Refrescos
2 - Papas 
3 - Pizzas

elige la opcion correcta: """

opcion = int(input(menu))

if opcion == 1:
    opciones('¿Cuanto te ha costado los refrescos?: ', 1.5)

elif opcion == 2:
    opciones('¿Cuanto te ha costado las papas?: ', 1.2)

elif opcion == 3:
    opciones('¿Cuanto te ha costado las pizzas?: ', 1.3)

else:
    print('No hagas trampas, solo opción 1, 2 y 3. ')




