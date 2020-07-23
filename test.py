import math

text_zahl = []
zahl = 0
for i in range(len(text)):
    print(text[i])
    try:
        int(text[i])
        text_zahl = text_zahl + [str(text[i])]
    except ValueError:
        None

print(text_zahl)
text_zahl.reverse()
multiplikator = [1, 10, 100, 1000, 10000, 100000, 1000000]
print(text_zahl)

for i in range(len(text_zahl)):
    zahl = zahl + int(text_zahl[i])*multiplikator[i]

print(zahl)