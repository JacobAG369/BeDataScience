#proyecto con validaciones

#aqui no agregamos validaciones
nom = input("Cual es tu nombre?: ")

#edades solo enteras, no negativas
while True:
    try:
        edad = int(input("Cual es tu edad?"))
        if edad <0:
            print("La edad no puede ser menor a zero")
        else:
            break
    except ValueError:
        print("Intentalo de nuevo, ingresa un valor adecuado porfavor")

#peso, solo valores entero y flotantes, mayores que 0

while True:
    try:
        peso = float(input("Ingresa tu peso en kg: "))
        if peso <= 0:
            print("El peso ingresado debe ser mayor que 0. Intenta de nuevo.\n")
        else:
            break
    except ValueError:
        print("Debes ingresar tu peso e kg (ej: 72 o 72.5). ")    

while True:
    try:
        altura = float(input("Ingresa tu altura en metros: "))
        if altura <= 0:
            print("Tu altura debe ser mayor a zero.")
        else:
            break
    except ValueError:
        print("Error, ingrese su estatura de manera correcta: (ej: 1.72 o 1.75). ")

IMC = peso / (altura **2)
IMC = round(IMC,2)

# Clasificación del IMC
if IMC < 18.5:
    clasificacion = "Bajo peso"
elif IMC < 25:
    clasificacion = "Peso normal"
elif IMC < 30:
    clasificacion = "Sobrepeso"
elif IMC < 35:
    clasificacion = "Obesidad I"
elif IMC < 40:
    clasificacion = "Obesidad II"
else:
    clasificacion = "Obesidad III"

# Reporte final
print("\n-------- PERFIL DEL USUARIO --------")
print(f"Nombre: {nom}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {IMC}")
print(f"Clasificación: {clasificacion}")
print("------------------------------------")