import xlrd
from io import open
import elementoPila
from lexico import analizador
from stack import stack
from sintactico import sintactico

analizador = sintactico()

analizador.compliador("imt suma ( int a , int b ) { return a + b ; } int main ( ) { int resultado ; resultado = suma ( 24 , 6 ) ; }")
#MASM
#int suma ( int a , int b ) { return a + b ; } int main ( ) { int resultado ; resultado = suma ( 24 , 6 ) ; }