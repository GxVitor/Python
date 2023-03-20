from datetime import date

ano_atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input(f"Em Que Ano a {c}° nasceu? "))
    idade = ano_atual - ano
    if idade <= 21:
        menor = menor + 1
    else:
        maior = maior + 1
        
print(f"Tem {menor} Menor de Idade e {maior} Maior de Idade")
