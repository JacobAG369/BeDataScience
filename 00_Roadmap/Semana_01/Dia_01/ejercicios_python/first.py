if 5 > 3:
    print("Five is greater than three.")

else:
    print("FIve is not gfreater than three")

#HOLA ESTO ES UNN COMENTARIO JEJE


"""
THIS IS A COMMENTBLOCK BECAUSE IM LEARNIGN THAT PYTHON J
"""


snake_case = "Para variables y funciones"

PascalCase = "Para clases"

CONSTANTE_EN_MAYUSCULAS = "Para constantes"

_atributoprivado1 = "Para atributos privados"

class_ = "Para evitar keyswords reservadas"

#el uso de doble guion bajo es para metodos especiales __init__
class Clase:
    def __init__(self):
            print("Init")


import pandas as pd

df = pd.read_csv("ventas.csv")
df.shape
(df.describe())













#strings
mi_string = "Hola, soy un string"
mi_string_doble = 'Hola, soy un string con comillas dobles'
mi_string_multilinea = """Hola,
soy un string
multilinea"""

mi_string_con_escape = "Hola, soy un string con una comilla doble: \" "

mi_string_raw = r"Hola, soy un string raw con una comilla doble: \" "

strng = "hola mundo"
float = 4.5
int = 4
boolean = True
NoneType = None


listas = {"Manzanas", "Naranjas", "Peras", "Limones"}

tuplas = ("Naranjas", "peras", "Limones", "manzanas")

deportes = {"futbol", "basquetbol", "futbol"}

i_set = {1, 2, 3, 4}

set()


diccionarios = {
     
     "nombre" : "Jimmy",
     "edad" : 25,
     "altura": 1.75

}

conjuntos = {"Manzanas", "Naranjas", "Peras", "Limones"}

rangos = range(0,10)
print(type(strng))
print(type(float))
print(type(int))
print(type(boolean))
print(type(NoneType))
print(type(listas))
print(type(tuplas))
print(type(diccionarios))
print(type(conjuntos))
print(type(rangos))
print(mi_string)
print(mi_string_doble)
print(mi_string_multilinea)
print(mi_string_con_escape)
print(mi_string_raw)
print(snake_case)
print(PascalCase)
print(CONSTANTE_EN_MAYUSCULAS)
print(_atributoprivado1)
print(class_)
objeto = Clase()

