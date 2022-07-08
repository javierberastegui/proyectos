def run():
    lista = [1, "Alto", False, 8.8]
    diccionario = {"firstname": "Javier", "lastname": "Berastegui"}
    

    super_lista = [
        {"Nombre": "Javier", "Apellido": "Berastegui"},
        {"Nombre": "Adrian", "Apellido": "Hernandez"},
        {"Nombre": "Kevin", "Apellido": "de la Rosa"},
        {"Nombre": "Asahel", "Apellido": "Garcia"},
        {"Nombre": "Alejandro", "Apellido": "Lorenzo"},
    ]

    super_diccionario = {
        "numero_decimal": [1.2, 2.5, 3.1, 2.2],
        "numero_negativos": [-1, -2, -4, -8],
    }

    for llaves, valores in super_diccionario.items(): # Recorrer llaves y valores
        print(llaves, "-", valores)

if __name__ == '__main__':
    run()