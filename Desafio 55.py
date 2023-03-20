#Ler o Peso de cinco pessoas, e mostra o maior peso e o menor
maior = 0
menor = 0

for p in range(1,6):
    peso = float(input(f"Peso da {p}° Pessoa: "))

    if p ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O Menor Peso foi  de {menor} e o maior foi {maior}")
