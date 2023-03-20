import random
from time import sleep

print('-=-' *20)
print("Jokenpô")
print("-=-" *20)

jogador = int(input("""Escolha uma opção
(0)Pedra
(1)Tesoura
(2)Papel
Qual A Sua Escolha: """))

print('-=-' *20)

intens = ("Pedra","Papel","Tesoura")
computador = random.randint(0,2)
maquina = intens[computador]

if jogador == 0 and maquina in "['Pedra']":
    print("Deu Empate")

elif jogador == 0 and maquina in "['Tesoura']":
    print(f"Parabens Você ganho eu Escolhi {maquina}")

elif jogador == 0 and maquina in   "['Papel']":
    print(f"Que Pena Você Perdeu eu Escolhi {maquina}")

elif jogador == 1 and maquina in   "['Pedra']":
    print(f"Que Pena Você Perdeu eu Escolhi {maquina}")

elif jogador == 1 and maquina in   "['Papel']":
    print(f"Parabens Você ganho eu Escolhi {maquina}")

elif jogador == 1 and maquina in   "['Tesoura']":
    print("Deu Empate")

elif jogador == 2 and maquina in   "['Pedra']":

    print(f"Parabens Você ganho eu Escolhi {maquina}")
    
elif jogador == 2 and maquina in   "['Tesoura']":

    print(f"Que Pena Você Perdeu eu Escolhi {maquina}")

elif jogador == 2 and maquina in   "['Papel']":
    print("Deu Empate")
    
    

print("-=-" *20)
print(maquina)