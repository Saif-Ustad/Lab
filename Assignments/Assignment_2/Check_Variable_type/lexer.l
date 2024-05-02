%{
%}

%%

"/*"([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*"*"+"/"   { printf("C comment : %s\n", yytext); }

"//".*   { printf("C++ comment : %s\n", yytext); }

[0-9]+ { printf("Number : %s\n", yytext); }

int|void|double|float|char { printf("Keyword : %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]* { printf("Identifier : %s\n", yytext); }

"+"|"-"|"*"|"/"|"=" { printf("Operator : %s\n", yytext); }

[\n\t ]+ { /* Ignore whitespace, newline, tab */ }

. { printf("Unknown : %s\n", yytext); }

%%

int yywrap() {
    return 1;
}

int main(int argc, char *argv[]) {
    ++argv, --argc;  /* skip over program name */
    if (argc > 0)
        yyin = fopen(argv[0], "r");
    else
        yyin = stdin;

    yylex();
}
