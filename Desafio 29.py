from time import sleep
c = float(input("Qual A sua Velocidade:"))
m = 7
ul = 80

if c >ul:
    v = (c-ul) * m
    print(f"Sua Velocidade Passou do Limite Sua Multa Sera de {v}")
else:
    print("Tudo Certo Pode Continuar Seu Passeio")
