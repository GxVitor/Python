n = int(input("Digite Uma Numero:"))
n1 = int(input("Digite Outro Numero:"))
n2 = int(input("Digite Outro Numero:"))

if n > n1 and n > n2:
    print(f"O Maior Numero é o {n}")

if n1 > n and n1 > n2:
    print(f"O maior numero é {n1}")

if n2 > n and n2 > n1:
    print(f"O maior Numero é o {n2}")

if n < n1 and n < n2:
    print(f"O Menor Numero é {n}")

if n1 < n and n1 < n2:
    print(f"O Menor Numero é {n1}")

if n2 < n and n2 < n1:
    print(f"O Menor Numero é {n2}")
