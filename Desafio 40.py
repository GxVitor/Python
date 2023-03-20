from time import sleep

print("-=-" *20)
print("Media de Alunos")
print("-=-" *20)

n1 = float(input("Digite a Primeira Nota:"))
n2 = float(input("Digite A Segunda Nota:"))
print("-=-" *20)
print("Analizando...")
sleep(1)

media = (n1 + n2) / 2

if media < 5.0:
    print(f" Sua media é {media}")
    print("Lamendo em Informa Mais Você Esta de Reprovado")

elif media >= 5.0 and media < 7.0:
    print(f" Sua media é {media}")
    print("Você Esta de Recuperação")

elif media > 7.0:
    print(f" Sua media é {media}")
    print("Parabens Você Passou")

print("-=-" *20)         