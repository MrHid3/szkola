import string

tekst = open("inwokacja.txt", "r",encoding="utf-8").read()

samogloski = ["a","e","i","o","u","y","ó","ą","ę"]
polskie = ["ą","ę","ó","ć","ł","ż","ź","ń"]
alfabet = ["a"]
ALFABET = ["A"]
POLSKIE = ["Ą","Ę","Ó","Ć","Ł","Ż","Ź","Ń"]
SAMOGLOSKI = ["A","E","I","O","U","Y","Ó","Ą","Ę"]
alfabet += polskie
ALFABET += POLSKIE
whitespace = string.whitespace


ileWielkich = 0
ileMalych = 0
ileWszystkich = 0
ileSamoglosek = 0
ileSpolglosek = 0
ileBialych = 0
ileZnakow = 0
ileWierszy = 0
ileLiter = 0

for letter in string.ascii_lowercase:
    alfabet.append(letter)

for letter in string.ascii_uppercase:
    ALFABET.append(letter)


print("Dla jakiej litery chcesz sprawdzić?")
dana = input()
ileLiter =  tekst.count(dana)
print(f"Litera {dana} pojawia się {ileLiter} razy")

for litera in alfabet+ALFABET:
        ile = tekst.count(litera)
        ileWszystkich += ile
        print(f"Litera {litera} pojawia się {ile} razy")
print(f"Litery pojawiły się {ileWszystkich} razy")

ile = 0
for litera in alfabet:
    ile = tekst.count(litera)
    ileMalych += ile
    print(f"Mała litera {litera} pojawiła się {ile} razy")
print(f"Małe litery pojawiły się {ileMalych} razy")

ile = 0
for litera in ALFABET:
    ile = tekst.count(litera)
    ileWielkich += ile
    print(f"Wielka litera {litera} pojawiła się {ile} razy")
print(f"Wielkie litery pojawiły się {ileWielkich} razy")


for letter in samogloski:
    alfabet.remove(letter)

for letter in SAMOGLOSKI:
    ALFABET.remove(letter)


ile = 0
for litera in samogloski+SAMOGLOSKI:
    ile = tekst.count(litera)
    ileSamoglosek += ile
    print(f"Samogłoska {litera} pojawia się {ileSamoglosek} razy")
print(f"Samogloski pojawiają się {ileSamoglosek} razy")

ile = 0
for litera in alfabet+ALFABET:
    ile = tekst.count(litera)
    ileSpolglosek += ile
    print(f"Spółgłoska {litera} pojawia się {ile} razy")
print(f"Spółgłoski pojawiły się {ileSpolglosek} razy")

ile = 0
for space in whitespace:
    ile = tekst.count(space)
    ileBialych += ile
print(f"W tym tekście mamy {ileBialych} białych znaków")

ile = 0
for znak in tekst:
    for letter in alfabet+ALFABET+samogloski+SAMOGLOSKI:
        if znak == letter:
            ile += 1
ileZnakow = ile
print(f"{ileZnakow} znaków to nie litery")

ileWierszy = tekst.count("\n")
print(f"Ten wiersz ma {ileWierszy} wierszy")


print("Tak więc, ten wiersz ma:")
print(ileWszystkich, " liter,")
print(ileMalych, " małych liter,")
print(ileWielkich, " wielkich liter,")
print(ileSamoglosek, " samogłosek,")
print(ileSpolglosek, " spółgłosek,")
print(ileBialych, " białych znaków,")
print(ileZnakow, " znaków które nie są literami,")
print(ileWierszy, " wierszy.")
print(f"W nim też litera {dana} pojawia się {ileLiter} razy")
