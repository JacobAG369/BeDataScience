"""Calcula el IMC desde la consola y muestra la clasificación."""

def leer_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor ingresa un número válido.")

def clasificacion_imc(imc: float) -> str:
    if imc < 18.5:
        return "Bajo Peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    if imc < 35:
        return "Obesidad I"
    if imc < 40:
        return "Obesidad II"
    return "Obesidad III"

def main() -> None:
    nombre = input("¿Cuál es tu nombre?: ")
    edad = leer_float("¿Cuál es tu edad?: ")
    peso = leer_float("¿Cuál es tu peso (kg)?: ")
    altura = leer_float("¿Cuál es tu altura (m)?: ")

    imc = round(peso / (altura**2), 2)
    clasificacion = clasificacion_imc(imc)

    print("\n---------- PERFIL DEL USUARIO ----------")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Peso: {peso}")
    print(f"Altura: {altura}")
    print(f"IMC: {imc}")
    print(f"Clasificación: {clasificacion}")
    print("---------- PERFIL DEL USUARIO ----------")

if __name__ == "__main__":
    main()