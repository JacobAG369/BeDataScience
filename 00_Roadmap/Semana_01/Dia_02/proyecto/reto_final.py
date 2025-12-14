productos = [
    {"nombre": "Laptop", "precio": 15000, "stock": 5},
    {"nombre": "Mouse", "precio": 250, "stock": 0},
    {"nombre": "Teclado", "precio": 600, "stock": 12},
    {"nombre": "Monitor", "precio": 3500, "stock": 7},
    {"nombre": "USB", "precio": 120, "stock": 0}
]

for p in productos:
    if p["stock"] == 0:
        print("Agotado:", p["nombre"])






def saludar(nombre):
    print("Hola", nombre)

saludar("Jimmy")
