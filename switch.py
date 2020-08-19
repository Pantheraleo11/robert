from mainfunktions import random_answer
from mainfunktions import team

def switch(message):
    m = message.content.split(" ")
    return {
        '/dice': random_answer.dice(message),
        '/coin': random_answer.coin(message),
        '/toss': random_answer.toss(message),
        '/team': team.team(message),
        '/team start': team.team_start(message),
    }.get(m[0])
