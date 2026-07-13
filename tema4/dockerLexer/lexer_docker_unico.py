import re


# Patrones reconocidos por el lexer.
TOKENS = [
    ("COMMENT", r"\#.*"),
    ("FROM", r"\bFROM\b"),
    ("RUN", r"\bRUN\b"),
    ("COPY", r"\bCOPY\b"),
    ("CMD", r"\bCMD\b"),
    ("WORKDIR", r"\bWORKDIR\b"),
    ("ENV", r"\bENV\b"),
    ("EXPOSE", r"\bEXPOSE\b"),
    ("STRING", r'"[^"\n]*"'),
    ("IMAGE", r"[A-Za-z0-9._/-]+:[A-Za-z0-9._-]+"),
    ("PATH", r"(?:/[\w.\-]+)+/?"),
    ("NUMBER", r"\b\d+\b"),
    ("WORD", r"[A-Za-z0-9_.:/\-]+"),
    ("LBRACKET", r"\["),
    ("RBRACKET", r"\]"),
    ("COMMA", r","),
    ("EQUALS", r"="),
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t\r]+"),
    ("MISMATCH", r"."),
]

TOKEN_REGEX = re.compile(
    "|".join(f"(?P<{nombre}>{patron})" for nombre, patron in TOKENS),
    re.MULTILINE,
)


def lexer(texto):
    """Analiza el texto y retorna token, lexema, línea y columna."""
    numero_linea = 1
    inicio_linea = 0

    for coincidencia in TOKEN_REGEX.finditer(texto):
        tipo = coincidencia.lastgroup
        lexema = coincidencia.group(tipo)

        if tipo == "NEWLINE":
            numero_linea += 1
            inicio_linea = coincidencia.end()
            continue

        if tipo in {"SKIP", "COMMENT"}:
            continue

        columna = coincidencia.start() - inicio_linea + 1

        if tipo == "MISMATCH":
            yield "ERROR_LEXICO", lexema, numero_linea, columna
        else:
            yield tipo, lexema, numero_linea, columna


def analizar(nombre, contenido):
    print("\n" + "=" * 72)
    print(nombre)
    print("=" * 72)
    print(contenido)

    print(f"{'TOKEN':<18} {'LEXEMA':<28} {'LÍNEA':<7} COLUMNA")
    print("-" * 72)

    errores = 0

    for tipo, lexema, linea, columna in lexer(contenido):
        print(f"{tipo:<18} {lexema:<28} {linea:<7} {columna}")

        if tipo == "ERROR_LEXICO":
            errores += 1

    print("-" * 72)

    if errores == 0:
        print("Resultado: archivo válido, sin errores léxicos.")
    else:
        print(f"Resultado: se encontraron {errores} error(es) léxico(s).")


# Tres ejemplos solicitados en la asignación.
EJEMPLO_1 = """\
FROM python:3.12
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 8000
CMD ["python", "app.py"]
"""

EJEMPLO_2 = """\
FROM ubuntu:22.04
WORKDIR /proyecto
COPY . /proyecto
ENV MODO=produccion
RUN echo "Instalando aplicación"
EXPOSE 8080
"""

EJEMPLO_3 = """\
FROM python:3.12
WORKDIR /app
COPY . /app
RUN echo "Prueba"
@
"""


if __name__ == "__main__":
    analizar("EJEMPLO 1: Dockerfile válido", EJEMPLO_1)
    analizar("EJEMPLO 2: Dockerfile válido", EJEMPLO_2)
    analizar("EJEMPLO 3: Dockerfile con error léxico", EJEMPLO_3)
