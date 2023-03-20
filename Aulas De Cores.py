#Texto/ fundo de tela
#30 Branco    40
#31 Vermelho  41
#32 Verde     42
#33 Amarelo   43
#34 Azul      44
#35 Roxo      45
#36 Ciano     46
#37 Cinza     46

#Texto
#0 Sem nada no Texto
#1 Bold (Negrito)
#4 Underline (Linha em Baixo)
#7 Negative

a = 3
b = 5
ver = '\033[31m' # Vermelho
azul = '\033[34m'


stopcolor = "\033[m"
print(f"Os Valores São {azul}{a}{stopcolor} e {ver}{b}{stopcolor}")