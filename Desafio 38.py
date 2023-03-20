from time import sleep

print("-=-" *20)
n1 = int(input("Digite Uma Numero:"))
n2 = int(input("Digite Outro Numero:"))
print("-=-" *20)
print("Carregando Dados...")
sleep(1)

if n1 > n2:
    print(f"O {n1} é o maior Numero")

elif n2 > n1:
    print(f" O {n2} é o Maior Numero!")

if n1 < n2:
    print(f" O {n1} é o Menor Numero!")

elif n2 <n1: 
    print(f"O {n2} é o menor Numero!")

elif n1 == n2:
    print(f"Os Dois Numeros São Iguais!!")

print("-=-" *20)

