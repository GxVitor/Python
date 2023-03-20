
s = ' '

while s != 'True':
    s = str(input("Digite Seu Sexo[M/F]: ")).upper()[0].strip()
    if s == 'M':
        s = 'True'
    if s == 'F':
        s = 'True'
    else:
        print("Sexo Invalido")
        
print("Sexo Registrado")

sexo = str(input("Informe seu Sexo: [M/F]: ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')

