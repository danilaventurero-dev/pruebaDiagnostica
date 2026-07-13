%{
#include <stdio.h>
%}

%option noyywrap

%%

"fn"            { printf("TOKEN: FN, Lexema: %s\n", yytext); }
"let"           { printf("TOKEN: LET, Lexema: %s\n", yytext); }
"if"            { printf("TOKEN: IF, Lexema: %s\n", yytext); }
"while"         { printf("TOKEN: WHILE, Lexema: %s\n", yytext); }
"return"        { printf("TOKEN: RETURN, Lexema: %s\n", yytext); }

[0-9]+          { printf("TOKEN: NUMBER, Lexema: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* {
                  printf("TOKEN: IDENTIFIER, Lexema: %s\n", yytext);
                }

"="             { printf("TOKEN: ASSIGN, Lexema: %s\n", yytext); }
">"             { printf("TOKEN: GREATER_THAN, Lexema: %s\n", yytext); }
"<"             { printf("TOKEN: LESS_THAN, Lexema: %s\n", yytext); }
"+"             { printf("TOKEN: PLUS, Lexema: %s\n", yytext); }
"-"             { printf("TOKEN: MINUS, Lexema: %s\n", yytext); }
"*"             { printf("TOKEN: MULTIPLY, Lexema: %s\n", yytext); }
"/"             { printf("TOKEN: DIVIDE, Lexema: %s\n", yytext); }

"("             { printf("TOKEN: LPAREN, Lexema: %s\n", yytext); }
")"             { printf("TOKEN: RPAREN, Lexema: %s\n", yytext); }
"{"             { printf("TOKEN: LBRACE, Lexema: %s\n", yytext); }
"}"             { printf("TOKEN: RBRACE, Lexema: %s\n", yytext); }
";"             { printf("TOKEN: SEMICOLON, Lexema: %s\n", yytext); }

[ \t\r\n]+      { /* Ignorar espacios y saltos de línea */ }

.               { printf("ERROR LEXICO: caracter no reconocido: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *archivo = fopen(argv[1], "r");

        if (archivo == NULL) {
            perror("Error al abrir el archivo");
            return 1;
        }

        yyin = archivo;
    }

    yylex();
    return 0;
}
