from time import sleep




programa = 0
maior = 0
menor = 0

while programa != 5:
    programa = int(input("""
[1]Soma
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do Pragrama
Escolha Uma Opção: """))
    if programa == 1:
        print("Ok Vamos Somar")
        n = int(input("Digite o Primeiro Numero: "))
        n1 = int(input("Digite o Segundo Numero: "))
        print(f"A Soma Entre {n} + {n1} é {n1 + n}")
        sleep(3)
    if programa == 2:
        print("Vamos Multiplicar Ent")
        n = int(input("Digite o Primeiro Numero: "))
        n1 = int(input("Digite o Segundo Numero: "))
        print(f"A Multiplicação de {n} . {n1} é {n * n1}")
        sleep(3)
    if programa == 3:
        print("Ok Vamos Descobrir o Maior Numero Digitado de 10 numeros ok")
        for c in range(1,11):
            numero = int(input((f"{c}°Numero: ")))     
            if c == 1:
                maior = numero
                menor = numero
            else:
                if numero > maior:
                    maior = numero
                if numero < menor:
                    menor = numero
        print(f"O Maior Numero Digitado é {maior} e o menor numero digitado é {menor}")   
    if programa == 4:
        n = int(input("Novo Numero?: "))       
    if programa > 5:
       print("Opção invalido Porfavor Digitar Novamente")
print("Fim")
