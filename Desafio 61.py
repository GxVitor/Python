print("Gerador de PA")
print('-=-' * 20)

primeiro = int(input("Primeiro Termo:"))
razão = int(input('Razão da PA:'))
cont = 1
termo = primeiro
while cont <= 10:
    print(f' {termo} ->', end='')
    cont += 1
    termo += razão
print('Fim')
