# Lexer para subconjunto de Rust usando Flex

## Archivos

- `lexer.l`: especificación del analizador léxico.
- `programa.rs`: archivo de prueba.

## Requisitos

En Ubuntu/WSL:

```bash
sudo apt update
sudo apt install flex gcc
```

## Generación y compilación

```bash
flex lexer.l
gcc lex.yy.c -o lexer
```

## Ejecución

```bash
./lexer programa.rs
```

## Archivos generados

- `lex.yy.c`: código C generado automáticamente por Flex.
- `lexer`: ejecutable Linux.
