def run():
    diccionario = {
        'Empresa1': 10000,
        'Empresa2': 35000,
        'Empresa3': 58952
    }

    for empresa, capital in diccionario.items():                      ## Consultar el nombre de las llaves 
        print(empresa + ' tiene ' + str(capital) + ' Euros')            ## y resultado de las mismas   
    


if __name__ == '__main__':
    run()