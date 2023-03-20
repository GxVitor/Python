salario = float(input("Digite Seu Salario:"))

if salario > 1250:
    au = (salario*10) / 100
    print(f"Seu Salario Vai ter um Aumento de 30% e seu salario atual ficara R${au+salario}")
else:
    au = (salario*30) / 100
    print(f"Seu Salria Tera Uma Aumento de 30% e seu Salario Atual Ficaram {au+salario}")
