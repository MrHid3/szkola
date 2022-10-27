print("Jakie liczby chcesz z zeuklidować?")
a = int(input())
b = int(input())
if a == 0:
    print(b)
    exit()
if b == 0:
    print(a)
    exit()
while a!=b:
    if a > b:
        a -= b
    else:
        b -= a 
print(a)