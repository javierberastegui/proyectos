def is_palindrome(string: str) -> bool:
    """Es verdadero o es falso"""
    string = string.lower() ## Minusculas
    string = string.replace(' ', '') # Quitar espacios
    return (string == string[::-1])


def run():
    palabra = input('Escribe un palindromo: ')
    print(is_palindrome(palabra))


if __name__ == '__main__':
    run()