def silnia(n):
    if n==0:
        return 1
    w = 1
    for  i in range(1, n+1):
        w = w * i
    print(w)
n = int(input("Jaką liczbe pragniesz zsilinić?"))
silnia(n)

#Ten program również był gotowy już w trakcie lekcji