somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ""
totmulher20 = 0
for p in range(1, 5):
    print(f"--------- {p}° Pessoa-----------")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print("A Media de Idade do grupo é de {} anos".format(mediaidade))
print("O Homem mais velho tem {} anos e se chama {}".format(maioridade, nomevelho))
print("Tem {} com menos de vinte anos".format(totmulher20))
