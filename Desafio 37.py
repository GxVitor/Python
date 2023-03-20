n1 = int(input("Digite um Numero inteiro: "))
base = int(input("""Escolha a opção que vc deseja converter
(1) Para Binário
(2) Para Octal
(3) Para Hexadecimal
Qual  A Sua escolha: """))

if base == 1: #Binário 
    print(f"{n1} convertido para Binário é {bin(n1)[2:]}")

elif base == 2:#Octal
    print(f"{n1} convertido para Octal é {oct(n1)[2:]}")


elif base == 3:#Hexadecimal
    print(f"{n1} convertido em Hexadecimal é {hex(n1)[2:]}")


else:
    print("Não tenho essa opção")