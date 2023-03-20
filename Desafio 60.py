

numero = int(input("Fatorial de: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)

numero2 = int(input("Fatorial de: ") )

resultado2=1
for n in range(1,numero2+1):
    resultado2 *= n

print(resultado2)