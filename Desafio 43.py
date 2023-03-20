from time import sleep
print("-=-" *20)
print("Calculador de IMC")
print("-=-" *20)

peso = float(input("Digite Seu Peso:"))
altura = float(input("Agora Digite Sua Altura:"))

imc = peso / (altura * altura)

print("-=-" *20)
print("Calcuclando.....")
sleep(1)

if imc < 18.5:
    print(f"Seu Imc é {imc:.2f} Você esta Abaixo do Peso")

elif imc < 25:
    print(f"Seu Imc é {imc:.2f} Você esta No Peso Ideal")

elif imc <30:
    print(f"Seu Imc é {imc:.2f} Vocé Esta Sobrepeso")

elif imc <40:
    print(f"Seu Imc é {imc:.2f} Vocé Esta Obesidade")

elif imc >40:
    print(f"Seu Imc é {imc:.2f} Você Esta na Obesidde Mórbida")   

print(f"o IMC é {imc:.2f}")
