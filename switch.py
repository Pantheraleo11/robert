from mainfunktions import random_answer

def switch(message):
    m = message.content.split(" ")
    return {
        '/dice': lambda: random_answer.dice(message),
        '/coin': lambda: random_answer.coin(message),
        '/toss': lambda: random_answer.toss(message)
    }.get(m[0])
