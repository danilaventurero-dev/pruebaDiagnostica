
#12+ 3 * (4)
cadena = input("Ingrese la expresion: ")
result = ""
i = 0
while i < len(cadena):
    caracter = cadena[i]
    # Ignorar espacios
    if caracter == " ":
        i += 1

    # NUMERO
    elif caracter.isdigit():

        numero = ""
        #numero += cadena[i]
        while i < len(cadena) and cadena[i].isdigit():
            numero += cadena[i]
            i += 1
        result += "NUMERO " + numero + " "
      
    # OPERANDO
    elif caracter.isalpha():
        operando = ""
        while i < len(cadena) and cadena[i] != " ":
            operando += cadena[i]
            i += 1
        result += "OPERANDO " + operando + " "

    # OPERADOR
    elif caracter == "+" or caracter == "-" or caracter == "*" or caracter == "/":
        result += "OPERADOR " + caracter + " "
        i += 1

    # PAREN_IZQ
    elif caracter == "(":
        result += "PAREN_IZQ " + caracter + " "
        i += 1

    # PAREN_DER
    elif caracter == ")":
        result += "PAREN_DER " + caracter + " "
        i += 1

    # ERROR
    else:
        result += "ERROR " + caracter + " "
        i += 1

print(result)