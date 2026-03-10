# Programa Calculadora com IF-ELIF-ELSE
#10/03/2025

op = input("Dígite 1-SOMA 2-SUBTRAÇÃO 3-MULTIPLICAÇÃO 4-DIVISÂO 5-POTENCIAÇÃO 6-RADICIAÇÃO")
op = int(op)

a = input("Entre com o 1º número")
a = int(a)

b = input ("|Entre com o 2º número")
b = int(b)

if (op == 1):
    print(a + b)
elif (op == 2):
    print(a - b)
elif (op == 3):
    print(a * b)
elif (op == 4):
    print(a / b)
elif (op == 5):
    print(a ** b)
else:
    print(a ** (1/2))
input() 

