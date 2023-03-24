import pandas as pd
import os
import time

# Nombramos el archivo.xlsx que quermos analizar
colegio = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRUwX-9fhwLH3YbShbc2emM4f-8JGlote6xdxR4UqVBsxax9Se13qfF_7ScL9XqKqnTKNvpck6gY6xU/pub?gid=0&single=true&output=csv") # Nombramos excel1
farmacia = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTgw8OsGxcF9lWLjyj3nE123urvxkTKfo74AIHs1rfNxcEyuLvD0B24lV2BQ7nP9-OUVzDof_oRl1v0/pub?gid=0&single=true&output=csv") # Nombramos excel2

# Realizamos formulas
colegio_y_farmacia = pd.concat([colegio['CN Colegio'].value_counts(), farmacia['CN Farmacia'].value_counts()], axis=1)
colegio_y_farmacia = colegio_y_farmacia.fillna(0)  # we put it up here before we opperate with it.

colegio_y_farmacia['Diferencia'] = colegio_y_farmacia.iloc[:, 1] - colegio_y_farmacia.iloc[:, 0] # con iloc acceces a indices por posicion en vez de nombre
resultado = colegio_y_farmacia[colegio_y_farmacia['Diferencia'] != 0]


def run():
   colegio.to_excel(r"C:/precintos/resultado.xlsx")

# Esperar 5 segundos
time.sleep(5)

# Forzar el guardado del archivo
with open(r"C:/precintos/resultado.xlsx", "a") as f:
    f.flush()

# Esperar 3600 segundos
time.sleep(3600)

# Eliminar el archivo de Excel
os.remove(r"C:/precintos/resultado.xlsx")

# Imprimir un mensaje de salida
print("El programa ha terminado.")

# Esperar a que el usuario pulse una tecla para salir
input("Presiona cualquier tecla para salir.")


if __name__ == '__main__':
    run()