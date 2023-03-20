import time
import os


def mao_pra_direita():
	print('     /o/ \o\ ')
	print('      |   |  ')
	print('     / \ / \ ')
    
os.system('cls')
def mao_pra_esquerda():
	print('     \o\ /o/ ')
	print('      |   |  ')
	print('     / \ / \ ')
os.system('cls')

while True:
	os.system('cls')
	mao_pra_direita()
	time.sleep(0.2)
	os.system('cls')
	mao_pra_esquerda()
	time.sleep(0.2)
os.system('cls')