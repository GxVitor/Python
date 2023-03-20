
n = int(input("Numero: "))
r = int(input("Digite A Razão: "))
décimo = n + (10 -1) * r
for c in range(n,décimo,r):
  print(c,end=" ")

#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.