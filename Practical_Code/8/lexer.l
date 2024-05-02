%{
#include <stdio.h>
%}

%%
"Destiny" { printf("Noun: %s\n", yytext); }
"Dread Run arrives" { printf("Verb: %s\n", yytext); }
"it" { printf("Pronoun: %s\n", yytext); }
"from" { printf("Preposition: %s\n", yytext); }
"same" { printf("Adjective: %s\n", yytext); }
"all the" { printf("Determiner/Article: %s\n", yytext); }
[\t\n]+ { /* ignore whitespace */ }
%%

int main()
{
    yyin = fopen("input.txt", "r");
    yylex();
    fclose(yyin);
    return 0;
}

int yywrap() {
    return 1; // Indicate that there are no more files to parse
}

