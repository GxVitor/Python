import math
num = float(input('Escolha um Angulo: '))
seno = math.sin(math.radians(num))
print(f'O Angulo de {num} tem o seno de {seno:.2f}')
coneso = math.cos(math.radians(num))
print(f'O coneso de {num} é {coneso:.2f}')
tangente = math.tan(math.radians(num))
print(f'A Tangente de {num} é {tangente:.2f}')
