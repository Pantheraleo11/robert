from random import randint

def dice(message):
    try:
        m = message.content.split(" ")
        multiplikator = int(m[1])
    except:
        multiplikator = 6
    number = randint(0, multiplikator)
    return "The dice says: " + str(number)

def coin(message):
    number = randint(1, 2)
    if number == 1:
        return "Head"
    if number == 2:
        return "Tail"

def toss(message):
    number = randint(1, 2)
    if number == 1:
        return "Head\ntoss a coin to your witcher"
    if number == 2:
        return "Tail\ntoss a coin to your witcher"

