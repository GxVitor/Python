import  random
m = 0,1,2,3,4,5
n = random.choice(m)

player = int(input("Digite Um Numero:"))
if player == n:
     print("Parabens Você Acerto o Numero")
else:
    print(f"Que Pena Vc errou o Numero o, O Numero Escolhido Era {n}")