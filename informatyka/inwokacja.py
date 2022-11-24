import string

tekst = open("inwokacja.txt", "r",encoding="utf-8").read()
samogloski = ["a","e","i","o","u","y","ó","ą","ę",]
polskie = ["ą","ę","ó","ć","ł","ż","ź","ń"]
alfabet = ["a"]
for letter in string.ascii_lowercase:
    alfabet.append(letter)
alfabet += polskie
spolgloski = alfabet
for letter in samogloski:
    spolgloski.remove(letter)
print(alfabet)

ileWszystkich = 0
ileSamoglosek = 0
ileSpolglosek = 0

for litera in alfabet:
    ile = tekst.count(litera)
    ileWszystkich += ile
print(ileWszystkich)

for litera in samogloski:
    ile = tekst.count(litera)
    ileSamoglosek += ile
print(ileSamoglosek)

for litera in spolgloski:
    ile = tekst.count(litera)
    ileSpolglosek += ile
print(ileSpolglosek)

