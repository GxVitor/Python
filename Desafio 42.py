from socket import INADDR_ALLHOSTS_GROUP


print("-=-" *20)
print("Analisador de Triângulos")
print("-=-" *20)

l1 = float(input("Digite Um Lado:"))
l2 = float(input("Digite Outro Lado:"))
l3 = float(input("Digite Outro Lado:"))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l1 == l3 and l3 == l2:
        print("Triangulo Iquilatero")

    elif l1 == l2 or l1 == l3 or l3 == l2:
        print("Triângulo Isóscoles")

    else:
        print("Triângulo Escalano")

else:
    print("Não pode Forma Uma triangulo")