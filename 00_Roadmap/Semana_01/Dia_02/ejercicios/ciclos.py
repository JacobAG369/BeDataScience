#condicionales y ciclos

#if 

edad = 20

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")



#elif

calificacicion = float(input("Ingresa tu calificición: "))

if calificacicion >= 95:
    print("Autonomo")
elif calificacicion >= 80:
    print("Destacado")
elif calificacicion >=70:
    print("Satisfactorio")

else:
    print("No aplica")



#for -> es para recorrer sobre los elementos de una lista

nombres = ["jimmy", "Jacob", "bosnia", "Durev"]

for n in nombres:
    print(n)

for i, n in enumerate(nombres):
    print(i,n)



empleado = {"nombre": "jimmy", "apellido": "Aviña", "edad": 20, "rol": "data analyst"}

for columna, fila in empleado.items():
    print(columna, "=>", fila)



#while

contador = 0

while contador < 5:
    print("número: ", contador)
    contador += 1



for i in range(1,20):
    if i % 2 == 0:
        print(i)


ventas = [120, 55, 300, 20, 500, 90, 10]
ventas_altas = []


for v in ventas:
    if v >= 100:
        ventas_altas.append(v)

        
        print(ventas_altas)


edades = [12, 25, 19, 40, 17, 18, 15, 30]
mayores = 0


for edad in edades:
    if edad >= 18:
        mayores += 1

print("La cantidad de mayores son: ", mayores)








