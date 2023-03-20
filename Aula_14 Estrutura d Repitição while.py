''' while == enquanto'''

'''portugol:

enquando não Maça
    se Chão
        passo
    se Bucaro
        Pula
    se Moeda
        pega
pega

python:

while not Maça:
    if Chão:
        passo
    if Buraco
        Pula
    if moeda
        pega
pega

'''

'''for c in range(1,10):
    print(c)
print("fim")'''

"""c = 1
while c < 10:
    print(c)
    c = c + 1
print("fim")"""


"""r = ' '
while r != 'S': #condição de parada
    n = int(input('Digite m Valor: '))
    r = str(input("Quer Continuar: ")).upper()
print("fim")"""

n = 1
par = impar = 0

while n != 0: # N diferente de 0 SIM!! executa N diferente de 0? não é igual a 0 então para de executar
    n = int(input('Digite um valor: '))
    if n !=0:
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
            
print(f"Você digitou {par} números pares e {impar} números ímpares!")
