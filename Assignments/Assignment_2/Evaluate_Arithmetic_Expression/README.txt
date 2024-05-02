#commands to run

STEP1 : flex calc.l
STEP2 : bison -dy calc.y
STEP3 : gcc lex.yy.c y.tab.c -o calculator.exe
STEP4 : ./calculator.exe