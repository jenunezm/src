def es_palindromo(texto):
    texto2 = ""
    texto1 = texto.lower()

    for valor in texto1:
        if valor != " ":
            texto2 += valor

    largo = len(texto2)

    texto1 = ""

    while largo > 0:
        largo = largo - 1
        valor1 = largo
        texto1 += texto2[valor1]

    indice = texto1.find(texto2)

    if indice == 0:
        return True
    else:
        return False


print("Reconocer", es_palindromo("Reconocer"))
print("AbbA", es_palindromo("AbbA"))
print("Amo la Paloma", es_palindromo("Amo la Paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print("Somos o no somos", es_palindromo("Somos o no somos"))
