print("Ile liczb chcesz sprawdzić?")
c = int(input())
b = []
x = 0
for i in range(c):
    print("Liczba ",i+1,":", end=' ')
    a = int(input())
    b.append(a)
    print( )
for i in range(len(b)):
    if b[i] > x:
        x = b[i]
print("Najwieksza jest", x)