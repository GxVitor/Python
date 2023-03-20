nome = str(input("Qual o Seu Nome")).lower().strip()

if nome == 'vitor':
    print('Que Nome Bonito')

elif nome == 'pedro' or nome =='maria' or nome == 'paulo':
    print("Seu Nome é bem popular no Brasil")

elif nome in 'ana cláudia jéssica juliana':
    print('Belo Nome Feminino')    

else:
    print("Seu Nome é Bem Normal!")

print(f"Tenha Um Bom dia, {nome.title()}!")    