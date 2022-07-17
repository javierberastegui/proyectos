DATOS = [
    {
        'nombre': 'Javier',
        'edad': 31,
        'organizacion': 'Diario 3',
        'puesto': 'Desarrollador',
        'habilidad': 'Python',
    },
    {
        'nombre': 'Maria',
        'edad': 78,
        'organizacion': 'Diario 3',
        'puesto': 'Limpieza',
        'habilidad': 'Organizacion',
    },
    {
        'nombre': 'Jose',
        'edad': 45,
        'organizacion': 'Diario 3',
        'puesto': 'Informatico',
        'habilidad': 'Python',
    },
    {
        'nombre': 'Ester',
        'edad': 38,
        'organizacion': 'Canal 7',
        'puesto': 'Camara',
        'habilidad': 'Adobe',
    },
    {
        'nombre': 'Luca',
        'edad': 17,
        'organizacion': 'Canal 7',
        'puesto': 'Desarrollador',
        'habilidad': 'HTML',
    },
    {
        'nombre': 'Elena',
        'edad': 29,
        'organizacion': 'Diario 3',
        'puesto': 'Profesora',
        'habilidad': 'Oficce',
    },
    {
        'nombre': 'Juan',
        'edad': 75,
        'organizacion': 'Diario 3',
        'puesto': 'Tecnico',
        'habilidad': 'Sistemas',
    },
    {
        'nombre': 'Fran',
        'edad': 33,
        'organizacion': 'Diario 3',
        'puesto': 'Desarrollador',
        'habilidad': 'Python',
    },
    {
        'nombre': 'Lucia',
        'edad': 41,
        'organizacion': 'Diario 3',
        'puesto': 'Desarrollador',
        'habilidad': 'Java',
    },
    {
        'nombre': 'Pablo',
        'edad': 73,
        'organizacion': 'Canal 7',
        'puesto': 'Crearivo',
        'habilidad': 'Photoshop',
    },
]

def run():

    # 1 Desarrolladores de Python
    desarrolladores_python = [trabajadores["nombre"] for trabajadores in DATOS if trabajadores["habilidad"] == "Python"]
   
   # 2 Trabajadores en Diario 3
    diario3 = [trabajadores["nombre"] for trabajadores in DATOS if trabajadores["organizacion"] == "Diario 3"]
    
    # 3 Mayores de 18 años 
    adultos =  [trabajadores["nombre"] for trabajadores in DATOS if trabajadores["edad"] > 18]
    
   # 4 Menores de 18 años 
    menores =  [trabajadores["nombre"] for trabajadores in DATOS if trabajadores["edad"] < 18]
   
   # 5 Añadir Jubilados a la lista si son mayores de 70
    jubilados = list(map(lambda trabajadores: trabajadores | {"jubilados": trabajadores["edad"] > 70}, DATOS))
    
    # 6 Mayores de edad por funciones de orden mayor 
    adulto = list(filter(lambda trabajadores: trabajadores['edad'] > 18, DATOS))
    
    # 6 Solamente quiero el nombre 
    adulto = list(map(lambda trabajadores: trabajadores['nombre'], adulto))

    for trabajadores in adulto:
        print(trabajadores)


if __name__ == '__main__':
    run()