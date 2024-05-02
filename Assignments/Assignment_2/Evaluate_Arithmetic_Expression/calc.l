/* lex program for  solving arithmatic expression  */

/* decleration section in this sections we will decleared the different  value and include the header file which we are using in this program to run this program */

%{
#include<stdio.h>
#include "y.tab.h"
extern int yylval;
%}

/* this sections is known as defined section in which we defined the rule and regulation of regular expression which will going to accept or not */
%%
[0-9]+ { 
          yylval=atoi(yytext);
          return NUMBER;
       }
[\t] ;
[\n] return 0;
. return yytext[0];
%%
int yywrap()
{
return 1;
}

