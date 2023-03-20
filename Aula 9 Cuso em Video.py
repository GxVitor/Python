#Manipulando Texto

#len(frase) Mostras Quandas Caraqueterias Tem a Frase
#frase.count('o') vai conta quantas letras tem na frases em base a letra dentro do ()
#frase.count('o,0,13') Conta com fatiamento
#frase.find('deo') vai encontrar a frase
#'Curso' in frase #vai fala se existi a palavra escrita

#Transformação

#frase.replace('Python','Android') vai trocar a palavra Python pra Android
#frase.upper() pra cima, vai ficar em Maiuscolo
#frase.lower() vai ficar em minisculas
#frase.capitalize() vai jogar todas as caraqueteries pra minisculas só a primeira palavra vai ficar maiuscola
#frase.title() vai ficar assim "A Oi Suave"
#frase.strip() vai remover os espaço to começo e no fim
#frase.rstrip() o R na frente do strip ele começa pela direita
#frase.lstrip() o L vai começar pela Esqueda

#Divisão

#frase.split() vai dividir considerando os espaços da frase

#Junção

#'-'.join(frase) vai junta com base nos espaço

frase = " João é bonito ".title()
print(frase)
cont = '/'.join(frase)
print(cont)
