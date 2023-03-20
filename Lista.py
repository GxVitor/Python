import random
res = str(input("Digite")).lower()
print(res)

n1 = str(input('Escolha um Nome '))
n2 = str(input('Escolha Um Nome '))
n3 = str(input('Escolha um nome '))
n4 = str(input('Escolha Um Nome '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(f'A ordem esta{lista}')

