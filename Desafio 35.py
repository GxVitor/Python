print("-=-" * 20)
print("Analisador de Triângulos")
print("-=-" * 20)
l1 = float(input("Digite Uma Numero:"))
l2 = float(input("Digite Uma Numero:"))
l3 = float(input("Digite Uma Numero:"))


if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Esses Numeros Podem Formar um Triangulo")

else:
    print("Esses Numeros Não podem formar um triangulo")