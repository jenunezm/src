salida = "salir"
operacion = ""
resultado = 0

num2 = 0

print("Bienvenidos a la calculadora CHANCHITO FELIZ\nPara Terminar escribe:  Salir")
print("Las operaciones son:  suma, resta, multi y div")
num1 = float(input("Ingresa número:> "))

while operacion != salida:
    operacion = input("Ingresa Operación:> ").lower()
    if operacion == "salir":
        break
    num2 = float(input("Ingresa siguiente número:> "))
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multi":
        resultado = num1 * num2
    elif operacion == "div":
        resultado = num1 / num2
    else:
        print(
            "Operación Invalida, \n Las operaciones validas son:  suma, resta, multi y div")
        continue

    print("El resultado es: " + str(resultado))
    num1 = resultado
