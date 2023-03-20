#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos

frase = str(input("Digite Uma Frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = " "

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    print(inverso)
    
if inverso == junto:
    print("Temos um Palíndromo!")
    
else:
    print("A Frase Digitada não é um Palíndromo!")
    print(junto)
