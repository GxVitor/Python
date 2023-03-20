import random
from time import sleep


numeros = 1,2,3,4,5,6,7,8,9,10 #random.randint(0,10)
computador = random.choice(numeros)

print(computador)

player = 0
contador = 0
print("-=-"*20)
print("Jogo Do Adivinhar o Numero")
print("-=-"*20)
sleep(2)
print("Ok O jogo Funciona Assim eu vou pensar em um jogo de 1 a 10 e vc temq ue adivinhar")
print("Pensando...")
sleep(3)
print("Ok Pode tentar Adividar o Número que eu pensei")

while player != computador:
    player = int(input("Numero: "))
    contador += 1
    if player < computador:
        print('O Numero que eu pensei é maior')
    elif player > computador:
        print('O Numero que eu pensei é menor')
    
    
print(f"Boa Você tentou {contador}")