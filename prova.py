mulher = 0
homem = 0
homemgosta = 0
mulhergosta = 0

for c in range(1,10+1):
    print(f"--------- {c}° Pessoa-----------")
    sexo = str(input("Sexo: [M/F] ")).strip()
    gosta = str(input("Gosta de Chocolate[S/N]: ")).strip()
    if sexo in 'Ff':
        mulher += 1
        if gosta in 'Ss':
            mulhergosta += 1
    if sexo in 'Mm':
        homem += 1
        if gosta in 'Ss':
            homemgosta += 1

porcentohomem = (homemgosta/homem) * 100
porcentomulher = (mulhergosta/mulher) * 100

print(f'Tem no total {homem} de homem e {porcentohomem}% deles gostão de chocolate')
print(f'Tem no total {mulher} de mulher e {porcentomulher}% deles gostão de chocolate')

