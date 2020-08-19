from mainfunktions import funktion
import random
from mainfunktions import log
import discord

async def team_start(message):
        log.write_log("team wird erstellt", message.author)
        await message.channel.send("Teamwahl wird gestartet")
        funktion.flag_team(1)

async def team(message):
        await message.channel.send("Teams werden gesucht")
        await message.channel.send("|")
        funktion.flag_team(0)
        user = open("user.txt", "r")
        userr = user.readlines()
        random.shuffle(userr)
        team1 = []
        team2 = []
        for n in range(len(userr)):
            if n % 2 == 1:
                team1 = team1 + [userr[n]]
            elif n % 2 == 0:
                team2 = team2 + [userr[n]]
        await message.channel.send("Speiler Team 1 :")
        for n in range(len(team1)):
            n = n + 1
            print(str(team1[n - 1]))
            await message.channel.send(team1[n - 1])
        await message.channel.send("|")
        await message.channel.send("Spieler Team 2 :")
        for n in range(len(team2)):
            n = n + 1
            await message.channel.send(team2[n - 1])
        await message.channel.send("|")
        await message.channel.send("Fertig")
        funktion.clear_user()
        log.write_log("Teamwahl beendet", "Bot")
