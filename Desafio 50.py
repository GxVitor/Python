
soma = 0
cont = 0
for c in range(1,7):
    n = int(input(f"Digite o {c} Numero: "))

    if n%2 == 0:
        soma += n
        cont += 1
        
print(f"Você digitou {cont} par e a soma deles é {soma}")


#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


