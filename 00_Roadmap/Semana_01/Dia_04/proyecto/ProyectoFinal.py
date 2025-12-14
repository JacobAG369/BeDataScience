ventas = [500, 1200, 300, 1500, 800, 2000, 50]
#función que cuenta el total de ventas
def total_ventas(ventas):
    total = 0
    for v in ventas:
        total += v
    return total
    
#función que cuenta el promedio de ventas
def promedio(ventas):
    total = total_ventas(ventas)
    return total /len(ventas)
#funcion que cuentas las ventas mas altas, considerando que arriba de mil

def ventas_altas(ventas):
    contador = 0
    for v in ventas:
        if v >= 1000:
            contador += 1
    return contador


print("REPORTE DE VENTAS")
print("-----------------")
print("Total de ventas:", total_ventas(ventas))
print("Promedio de ventas:", promedio(ventas))
print("Ventas mayores a 1000:", ventas_altas(ventas))
