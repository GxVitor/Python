import math
import random
import audioop

n = float(input('Digite Uma Número: '))
print(f'Esse Número inteiro fica assim {math.floor(n)}')

#Toma no Cu pitaguras a² = b² + c²

print('=' * 40)
print('Vamos Achar a hipotenusa de um Triângulo retângulo')

c = float(input('Qual o Valor do Catedo oposto? '))
ca = float(input('Qual o Valor do Catedo Adejacente? '))
h1 = math.pow(c, 2)
h2 = math.pow(ca, 2)
h3 = (h1 + h2)
h4 = h3 ** (1/2)
con = (math.pow(c, 2) + math.pow(ca, 2)) ** (1/2)
print(f'Resultado {h4:.2f} ou {con}')

print('=' * 40)
nome1 = input('Escolha um nome: ')
nome2 = input('Escolha outro nome: ')
nome3 = input('Escolha outro nome: ')
nome4 = input('Escolha outro nome: ')
lista = [nome1, nome2, nome3, nome4]
r = random.choices(lista)
print(f'{r}')
