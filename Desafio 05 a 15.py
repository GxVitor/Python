n1 = int(input('Digite Um Numero: '))
s1 = n1 + 1
s2 = n1 - 1
s3 = n1 * 2  # Duplo
s4 = n1 * 3  # Tripo
s5 = n1 ** (1 / 2)  # Raiz Quadrada

print(f'Antes do {n1} vem o {s2} e depois do {n1} vai ser {s1}')
print(f'O Duplo de {n1} é {s3} e o tripo é {s4} e a raiz de {n1} é {s5}')
print('Vamos Calcular a media entre dois Números')
m1 = float(input('Digite um Número: '))
m2 = float(input('Digite Outro Número: '))

media = (m1 + m2) / 2  # media entre 2 números

print(f'A Media é {media:.1f}')
print('Vamos Trnformar metros em centimetro e milimetro')
m = float(input('Digite a Quantidade de metro para ser convertido: '))

# metros for centimetro 1m = 100cm

cm = m * 100
mm = m * 1000

print(f'{m} em Centimetro é {cm:.0f} e em milimetros é {mm:.0f}')
print('======================================')
print('Vamos Fazer a Tabuada ')

t = int(input('Digite um Número para nós fazemos a tabuada: '))

t1 = t * 1
t2 = t * 2
t3 = t * 3
t4 = t * 4
t5 = t * 5
t6 = t * 6
t7 = t * 7
t8 = t * 8
t9 = t * 9
t10 = t * 10

print(
    f'a Tabuada te {t} é \n{t}*1={t1}\n{t}*2={t2}\n{t}*3={t3}\n{t}*4={t4}\n{t}*5={t5}\n{t}*6={t6}\n{t}*7={t7}\n{t}*8={t8}\n{t}*9={t9}\n{t}*10={t10}')
print('========================')
print('Vamos contar quandos Dolar vc pode comprar com rais ')
r = float(input('Quandos Reias vc tem? R$'))

do = r / 3.27

print(f'Vc tem {do:.2f} em Dolar')
print('===================')
print('Vamos Calcular quanto de tinta vamos usar para pintar um parede')

p1 = float(input('Qual a Base da Parede? '))
p2 = float(input('Qual a altura da Parede? '))

# 1l pinta 2m de parede

parede = (p1*p2)/2

print(f'Para pintar a sua parade vc vai gastar {parede:.2f}L de tintas')
print('===========================')
print('Vamos Calcular 5% De Desconto ')

des = float(input('Qual o Preço do Produto? '))

desc = (des*5)/100
per = des-desc

print(f'5% de Desconto de {des} é {desc:.2f} o valor do produto custa {per:.2f}')
print('==============')
print('Vamos calcula o seu salario mais com 15% de aumento')

sa = float(input('Digite Seu Salario: '))

al = (sa*15)/100
almento = sa+al

print(f'O Salario de {sa} com o aumento de 15% é de {almento}')
print('=' * 20)
print('Vamos Conveter cº em fº')

c = float(input('Quandos Graus Cº esta ai? '))
c2 = (c/5) * 9
f = c2 + 32
print(f'Sabendo que estar {c} Graus então estar {f}Fahrenheit ')
print('=' * 20)
print('Vamos Calcular quando vai custar um alugueu de carro ')
dias = int(input('Quandos Dias vc Alugou o carro? '))
km = float(input('Quandos KM vc andou com o carro? '))

cus1 = dias * 60
cus2 = km * 0.15
cus3 = cus1 + cus2
print(f'O Valor fica {cus3}')


