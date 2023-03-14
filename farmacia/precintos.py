import pandas as pd

# Nombramos el archivo.xlsx que quermos analizar
colegio = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQZAd-7nf7zBS3-bi4AkTUS2Jhbu4HewL7ZdaGrU9NkDg33B1c6XN6K8j9gH_m2LuxXnKpTXlE2rRPl/pub?gid=0&single=true&output=csv") # Nombramos excel1
farmacia = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT8PEWirtYpcL9rRSIMUSP7wceQDiJFcqrXuBKuYgLTwltQ74mhIBiNKz-J_X8TRw9fkvJ681JksnOb/pub?gid=0&single=true&output=csv") # Nombramos excel2

# Realizamos formulas
colegio_y_farmacia = pd.concat([colegio['CN Colegio'].value_counts(), farmacia['CN Farmacia'].value_counts()], axis=1)
colegio_y_farmacia = colegio_y_farmacia.fillna(0)  # we put it up here before we opperate with it.

colegio_y_farmacia['Diferencia'] = colegio_y_farmacia.iloc[:, 1] - colegio_y_farmacia.iloc[:, 0] # con iloc acceces a indices por posicion en vez de nombre
resultado = colegio_y_farmacia[colegio_y_farmacia['Diferencia'] != 0]

def run():
   colegio.to_excel(r"C:/precintos/resultado.xlsx")

if __name__ == '__main__':
    run()