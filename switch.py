from mainfunktions import random_answer

def switch(message):
    m = message.content.split(" ")
    return {
        '/dice': random_answer.dice(message),
        '/coin': random_answer.coin(message),
        '/toss': random_answer.toss(message),
    }.get(m[0])
