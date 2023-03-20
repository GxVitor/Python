print("Gerador de PA")
print('-=-' * 20)

primeiro = int(input("Primeiro Termo:"))
razão = int(input('Razão da PA:'))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f' {termo} ->', end='')
        cont += 1
        termo += razão
    print(' Pausa')
    mais = int(input("Quantos termos você quer a mais? "))
print(f'Progressão finalizada com {total} termos mostrados')
