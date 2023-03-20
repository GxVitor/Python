from time import sleep
from datetime import date

print("-=-" *20)
print("Alistamento Militar")
print("-=-" *20)

ano = int(input("Que Ano Você Naceu?:"))
sexo = str(input("""Qual o Seu Sexo
Masculino
Feminino
""")).lower()

print("-=-" *20)
print("Carregando...")
sleep(1)
print('-=-' *20)
ali = ano + 18
ano_de_hoje = date.today().year

if sexo == 'masculino':

    if ali == ano_de_hoje:
        print("Você devera de alistar Nesse Ano Boa Sorte! ")

    if ali > ano_de_hoje:
        print(f"Você ainda não precisa de alistar só em {ali}")

    elif ali < ano_de_hoje:
        print(f"Já Passau da Hora de você se alistar! Você Deveria ter se alistado em {ali}")

else:
    print("Você não precisa se alistar")