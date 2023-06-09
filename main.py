from lexer import Lexer
from parser import Parser

text_input = """
print(2 == 4)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()


## DICCIONARIO ##
# *************************Caracteres*************************************

# num = "0123456789"
# may = 'A'..'Z'
# min = 'a'..'z'

# *************************Tipos de Datos*************************************
# int = num+
# string = ( may+ | min+ )
# real = num+.num+

# *************************Palabras Reservadas*************************************
# program
# if
# else
# then
# do
# while
# end
# print
# and
# or
# int
# string
# real
# bool
# true
# false
# for
# main

# *************************Operadores Aritmeticos*************************************
# +
# -
# *
# /

# *************************Operadores Relacionales*************************************
# <
# >
# !=
# ==
# >=
# <=

# *************************Parentesis y otros*************************************

# (
# )
# #
# {
# }
# ;
# .
# "
# ,
# =

# *************************Programa Ejemplo*************************************
# program main
# int :: i,n,f,x
# print("texto dump")
# f=5
# x=1
# for (x;x<f;x=x+1){
# 	n = x + f
# }
# print(n)
# end program main

# *************************Programa Ejemplo 1*************************************
# program main
# int :: i,n,f,x
# print("texto dump")
# f=1
# x=5
# if( x > f) then 
# {
# 	n = x + f
# }else{
# 	n = x - 4
# }

# print(n)
# end program main

# *************************Programa Ejemplo 2*************************************
# program main
# int :: i,n,f,x
# print("texto dump")
# f=1
# x=5
# while (x<f) do
# {
# 	x = f + 2
# }
# print(n)
# end program main