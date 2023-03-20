def contador(n):
    print(n)
    if n < 10:
        return(contador(n + 1))
contador(1)