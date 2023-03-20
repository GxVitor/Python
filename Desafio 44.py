
print("{:=^40}".format('Caixa'))


produto = float(input("Qual o Valor do Produto: R$"))
condicao = int(input("""Qual a forma de pagamento? 
(1)á vista Dinheiro/cheque
(2)á vista Cartão
(3)2x no Cartão
(4)3x ou mais no Cartão
Qual é a opção? """))

if condicao == 1:
    des = (produto*10) / 100 - produto
    print(f"No Dinheiro e Cheque Você ganha um Descondo de 10% o Seu Produto Custara {des * -1}")

elif condicao == 2:
    des = (produto*5) / 100 - produto
    print(f"No Cartão vc Ganha um desconto de 5% o preço do protudo ficara {des * -1}")

elif condicao == 3:
    print(f"o Valor do Produto é {produto}")

elif condicao == 4:
    juros = (produto*20) / 200 + produto
    print(f"3x ou Mais no Cartão tem um juros de 20% o Preço do Protudo ficara {juros}")
else:
    print("Infelizmente não temos essa opção")
 
