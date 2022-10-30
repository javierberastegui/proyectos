def run():
    peso = int(input("¿Cuanto pesa usted? "))
    if peso < 50:
        print("Debe usted subir de peso.")
    
    elif peso == 50:
        print("Esta en su pedo ideal.")

    else:
        print("Debe usted bajar de peso.")

if __name__ == '__main__':
    run()