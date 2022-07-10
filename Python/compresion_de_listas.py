# Sin comprension de listas 

def run():
    cuagrados = []
    for i in range(1, 70):
        if i % 3 != 0:
            cuagrados.append(i**6)

    print(cuagrados)


if __name__ == '__main__':
    run()