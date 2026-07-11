import turtle


# Producciones del lenguaje y parámetros de cada figura
GRAMATICA = {
    "CUADRADO": {
        "cadena": "acacacact",
        "angulo": 90
    },
    "TRIANGULO": {
        "cadena": "acacact",
        "angulo": 120
    },
    "LINEA": {
        "cadena": "aaaat",
        "angulo": 0
    }
}


def interpretar(cadena, angulo):
    """
    Interpreta una cadena del lenguaje de dibujo.

    a = avanzar
    c = girar
    g = desplazarse sin dibujar
    t = finalizar
    """

    lapiz = turtle.Turtle()
    lapiz.speed(3)

    for simbolo in cadena:

        if simbolo == "a":
            lapiz.forward(100)

        elif simbolo == "c":
            lapiz.right(angulo)

        elif simbolo == "g":
            lapiz.penup()
            lapiz.forward(40)
            lapiz.pendown()

        elif simbolo == "t":
            print("Figura terminada.")


def main():
    print("Figuras disponibles:")

    for figura in GRAMATICA:
        print("-", figura)

    opcion = input("\nSeleccione una figura: ").upper()

    produccion = GRAMATICA.get(opcion)

    if produccion is None:
        print("La figura seleccionada no existe.")
        return

    cadena = produccion["cadena"]
    angulo = produccion["angulo"]

    print("\nDerivación seleccionada:")
    print(f"<INICIO> -> <{opcion}> -> {cadena}")

    interpretar(cadena, angulo)

    turtle.done()


if __name__ == "__main__":
    main()