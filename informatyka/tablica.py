
import random

def koloruj(r,g,b,text):
    return f"\033[38;3;{r};{g};{b}m{text}\033[0m"

def tablica(n):
    for x in range(1,n+1):
        for y in range(1,n+1):
            wynik = x*y
            print(koloruj(random.randint(40,47), random.randint(40,47), random.randint(40,47), wynik), end=" ")
        print()

n = int(input("Podaj liczbę:\t"))

tablica(n)

#Miałem ten program gotowy na lekcji, przesyłam teraz, ponieważ
#nie zdążyłem go panu pokazać