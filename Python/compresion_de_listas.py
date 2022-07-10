# La magia de comprension de listas 😁😁

def run():
#    cuagrados = []
#    for i in range(1, 70):
#        if i % 3 != 0:
#            cuagrados.append(i**6)

    cuadrados = [i**6 for i in range(1, 70) if i % 3 != 0]

    print(cuadrados)


if __name__ == '__main__':
    run()