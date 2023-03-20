km = float(input("Qual A Distancia da Sua Viajem:"))
#v = km * 0.50
#v2 = km * 0.45

if km <= 200:
    v = km * 0.50
    print(f"A Sua Viajem Custara R${v}")
    print(f"deu {km*0.50:.2f}")
else:
    v = km * 0.45
    print(f"Sua Viajem Custa Mais Barata Por Ser Mais Longe o Valor Ficara R${v}")