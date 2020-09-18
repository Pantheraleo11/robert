from mainfunktions import random_answer
from mainfunktions import help

def switch(message):
    m = message.content.split(" ")
    return {
        '/help': help.help(message),
        '/dice': random_answer.dice(message),
        '/coin': random_answer.coin(message),
        '/toss': random_answer.toss(message),
    }.get(m[0])
