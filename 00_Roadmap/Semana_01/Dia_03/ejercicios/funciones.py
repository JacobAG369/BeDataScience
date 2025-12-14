#mi primera función
def saludar():
    print("Hola, desde una función")


#funcion con parametros
def saludar(nombre):
    print("Hola", nombre)

saludar("Jimmy")

#funcion que regresan valores con return
def sumar (a,b):
    result = a + b 
    return result

x = sumar(5,20)
print(x)

#calular precio con IVA
def precio_con_iva(precio):
    return precio * 1.16
#filtrar un valor
def es_caro(precio):
    return precio > 1000
#limpiar datos
def limipar_texto(t):
    return t.strip().lower()

x = 10 #variable global

def funcion():
    x = 5 #variable local del metodo
    print("dentro:", x)

funcion()
print("fuera:", x)



