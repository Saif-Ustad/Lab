/* yacc program for soving arithmatic expression */

/* decleration section in this sections we will decleared the different  value and include the header file which we are using in this program to run this program */
%{
    #include<stdio.h>
    int flag=0;
    
%}



%token NUMBER

%left '+' '-' 
%left  '*' '/' '%'
%left '(' ')'

/* this sections is known as defined section in which we defined the rule and regulation of regular expression which will going to accept or not */
%%
ArithmeticExpression: E{
         printf("\nResult=%d\n",$$);
         return 0;
        }
E:E'+'E {$$=$1+$3;}
 |E'-'E {$$=$1-$3;}
 |E'*'E {$$=$1*$3;}
 |E'/'E {$$=$1/$3;}
 |E'%'E {$$=$1%$3;}
 |'('E')' {$$=$2;}
 | NUMBER {$$=$1;}
;
%%

void main()
{ 
   printf("\nEnter Any Arithmetic Expression which can have operations Addition, Subtraction, Multiplication, Divison, Modulus and Round brackets:\n");
   yyparse();
  if(flag==0)
   printf("\nEntered arithmetic expression is Valid\n\n");
  
}

void yyerror()
{
   printf("\nEntered arithmetic expression is Invalid\n\n");
   flag=1;
}


