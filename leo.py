from distutils.command.clean import clean
from time import sleep
import os
from turtle import clear

print("Ola Jogador")
sleep(3)
os.system('cls')
nome = str(input("Qual o Seu nome?:"))
sleep(3)
os.system('cls')
print(f"Prazer em te conhecer {nome} vou te fazer um pergunta e vc vai responder ok? ")
sleep(3)
os.system('cls')
res = str(input("OK? ou Não: ok/não ")).lower()
if res == 'ok':
    per = str(input("Você Gosta de Pão ? s/n")).lower()
    if per == 'n':
        print("Você é mal amado")
        sleep(3)
    else:
        print("Boa Mlk")
        sleep(3)
elif res == 'não':
    print("Ent Vai Dormi Tchau")
    sleep(3)
else:
    print("Que porra vc digito? ")
    sleep(3)
    
os.system('cls')
print("Vai Dormi")

    
    