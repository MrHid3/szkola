import base64

key = 0x584b51f48bca9572acd08d378362
text = 0x2e2e3f9dabbcfc16c5f0fb5ee00b

xor = key ^ text

h = str(hex(xor)).upper()

print(h)

wynik = h[2:]

print(base64.b16decode(wynik))

# Pozdrowienia z Bali
# bozgi
