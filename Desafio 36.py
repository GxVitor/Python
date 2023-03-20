print("-=-" *20)
print("Empréstimo Bancário")
print("-=-" *20)

casa = float(input('Qual o Valor da Casa: '))
salario = float(input('Qual o Seu Salario: '))
anos = int(input("Em Quandos Anos Você quer paga o emprestimo? "))

prestação = casa/ (anos * 12)
minimo = salario*30 / 100


if prestação <= minimo :
    print("Certo Empréstimo pode ser CONCEDIDO")

else:
    print("Infelizmento não pode Você um empréstimo acima de 30% do seu salario ")
