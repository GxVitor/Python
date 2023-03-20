

from ast import Num
soma = 0
num = 0
total = 0
while num != 999:
    per = int(input("Digite Um Numero [999 para parar]: "))
    if per != 999:
        soma += per
        total += 1
    else:
        num = per
print(f"A Soma dos {total} Digitado é {soma} ")