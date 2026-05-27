cadena = input("Ingrese la expresion: ")

result = ""
espacio = 0
turno = 0
guiones = 0
piezas = 0
coordenada = 0
halfmove = 0
fullmove = 0
enroque = 0

i = 0
#rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq e3 0 1

def isValidFen(a):
   if a.lower() in "prnbqkPRNBQK":
       return True
   return False

def isValidTurn(a):
   if a.lower() in "wb":
       return True
   return False

def haveEnroque(a):
   if a.lower() in "KQkq":
       return True
   return False


while i < len(cadena):
    caracter = cadena[i]
    #valido si las letras usadas en el tablero(pre espacio) son validas en la nomenclatura fen
    if caracter.isalpha() and isValidFen(caracter) and espacio == 0:
        piezas+=1
        i+=1
        continue
    #valido guiones para asegurarme que cuenta con el numero de filas del tablero
    elif caracter == "/":
        guiones += 1
        i+=1
        continue
    #valido si es un numero, sin embargo creo q casos donde la columna tiene combinacion de espacios vacios y piezas puede fallar
    elif caracter.isdigit():
        if int(caracter) <= 8 and int(caracter) >= 0:
            i+=1
            continue
        else:
            #pending logic
            i+=1
            continue
    #Muy parecido a los guones los espeacios en blanco los uso para ubicarme dentro de la nomenclatura
    if caracter == " ":
        espacio+=1
        i+=1
        continue
    elif caracter.isalpha() and isValidTurn(caracter):
        turno+=1
        i+=1
        continue
    elif caracter.isalpha() and haveEnroque(caracter):
        enroque += 1
        i+=1
    elif caracter.isalpha() and espacio == 3:
        coordenada+=1
        i+=1
        continue
    elif caracter.isdigit() and espacio == 4:
        halfmove+=1
        i+=1
        continue
    elif caracter.isdigit() and espacio == 5:
        fullmove+=1
        i+=1
        continue
    elif caracter == "-":
        i+=1
        continue
    else:
        print("caracter desconocido" + caracter)


if espacio == 5 and guiones == 7 :
    print("true")


    
#rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq e3 0 1