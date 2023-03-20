nome = input('Digite Seu Nome!').strip()
d = nome.split()

print(f'Seu Nome em Minúsculas é {nome.lower()}')
print(f'Seu Nome em Maiúsculas é {nome.upper()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")}')
print(f'Seu Primeiro Nome tem {nome.find(" ")}')

num = int(input('Digite Um Numero'))
u = num // 1 % 10
z = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'A Unidade de {num} é {u}')
print(f'A Dezena de {num} é {z}')
print(f'A Centena de {num} é {c}')
print(f'O Milhar de {num} é {m}')

city = input("Qual o Nome da Sua Cidade").upper()
print('SANTO'in city)

nome2 = input('Digite seu Nome').strip()
#nome2 = nome2.strip()
#nome2 = nome2.lower()
print('silva'in nome2.lower())

frase = input('Digite um Frase')
frase = frase.strip()
frase = frase.lower()
letraa = frase.count('a')
print(f'tem {letraa} A na sua frase')
print(f'A primeira Letra A apareceu na posição {frase.find("a") + 1}')
print(f" A ultima letra A apareceu na Posição {frase.rfind('a') + 1}")

#Vitor Gabriel de Oliveira Duarte
nome3 = input('Digite seu Nome')
nome3 = nome3.strip()
nome3 = nome3.split()

print(f'Seu Primeiro Nome é {nome3[0]}')
print(f"Seu Ultimo Nome é {nome3[len(nome3) - 1]}")
