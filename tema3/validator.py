import re

regex = r"([a-h][1-8])|(N[a-h][1-8])|(B[a-h][1-8])|(O-O)"

print("Reconocimiento de movimientos PGN")

movimiento = input("Ingrese un movimiento: ")

if re.fullmatch(regex, movimiento):

    print("\nMovimiento válido.")

else:

    print("\nMovimiento inválido.")