maior = 0
menor = 0

for p in range(1,4):
    numero = int(input(f"{p}° Numero: "))

    if p ==1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f"O Menor Numero foi de {menor} e o maior foi {maior}")