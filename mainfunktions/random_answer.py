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

def random(message):
    try:
        m = message.content.split(" ")
        start = int(m[1])
        stop = int(m[2])
    except:
        start = 1
        stop = 6

    r = str(randint(start, stop))
    return r
