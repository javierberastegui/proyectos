def run():
    cuagrados = []
    for i in range(1, 250):
        if i % 3 != 0:
            cuagrados.append(i**6)

    print(cuagrados)


if __main__ == '__name__':
    run()