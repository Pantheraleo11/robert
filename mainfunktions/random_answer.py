from random import randint

def dice(message):
    if message.content == "/dice":
        multiplikator = 6
    else:
        m = message.content.split(" ")
        multiplikator = int(m[1])
    number = randint(0, multiplikator)
    await message.channel.send("The dice says: " + str(number))

def coin(message):
    zahl = random.randint(1, 2)
    if zahl == 1:
        await message.channel.send("Head")
    if zahl == 2:
        await message.channel.send("Tail")

def toss(message):
    number = random.randint(1, 2)
    if number == 1:
        await message.channel.send("Head")
    if number == 2:
        await message.channel.send("Tail")
    await message.channel.send("toss a coin to your witcher")
