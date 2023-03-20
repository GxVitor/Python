from datetime import date

print("-=-" *20)
print("Categoria de Natação")
print("-=-" *20)

ano = int(input("Em que Ano vc Naceu?:"))
print("-=-" *20)
ano_atual = date.today().year

idade = (ano - ano_atual) * -1

mirim =  9
infantil =  14
junior = 19
senior = 25
 
if idade <= mirim:
    print(f"O atleta tem {idade}")
    print("Voce Se Classicica como Mirim")

elif idade <= infantil:
    print(f"O atleta tem {idade}")
    print("Voce Se Classicica como Infantil")

elif idade <= junior:
    print(f"O atleta tem {idade}")
    print("Voce Se Classicica como Junior")

elif idade <= senior:
    print(f"O atleta tem {idade}")
    print("Voce Se Classicica como Senior")

elif idade > senior:
    print(f"O atleta tem {idade}")
    print("Voce Se Classicica como Master")            
