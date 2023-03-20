import random

bonito = ['sim','não']

pessoa = str(input("Digite Seu Nome Completo:")).lower()
sera = random.choice(bonito)
if pessoa == 'vitor gabriel':
    print("Voce é bonito")
elif sera == 'não':
    print("Que Pena Você é feio")
else:
    print("Voce é bonito")
    
