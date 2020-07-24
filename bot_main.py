import discord
import random
import funktion
import log


class MyClient(discord.Client):
    #login
    async def on_ready(self):
        print("I'm lock in. Beep bop.")
        log.write_log("bot on","bot")
        funktion.flag_sero(0)
        print(funktion.flag_team(2))

    async def on_message(self, message):
        if message.author == client.user:
            return

        #help anfragen
        if message.content.startswith("bot help team"):
            await  message.channel.send(funktion.help("team"))
        elif message.content.startswith("bot help random"):
            await  message.channel.send(funktion.help("random"))
        elif message.content.startswith("bot help") or message.content.startswith("help"):
            await message.channel.send(funktion.help("help"))

        #team /team wahl
        if message.content.startswith("bot team start") and funktion.flag_team(2) == 1:
            await message.channel.send("Loking for team")
            await message.channel.send("|")
            funktion.flag_team(0)
            user = open("user.txt","r")
            userr = user.readlines()
            random.shuffle(userr)
            team1 = []
            team2 = []
            for n in range(len(userr)):
                if n % 2 == 1:
                    team1 = team1 + [userr[n]]
                elif n % 2 == 0:
                    team2 = team2 + [userr[n]]
            await message.channel.send("Player Team 1 :")
            for n in range(len(team1)):
                n = n + 1
                print(str(team1[n-1]))
                await message.channel.send(team1[n-1])
            await message.channel.send("|")
            await message.channel.send("Player Team 2 :")
            for n in range(len(team2)):
                n = n + 1
                await message.channel.send(team2[n-1])
            await message.channel.send("|")
            await message.channel.send("Done!")
            funktion.clear_user()
            log.write_log("Team select finished", "Bot")

        #team
        elif message.content.startswith("bot team"):
            log.write_log("Team selection started", message.author)
            await message.channel.send("Team selection started")
            funktion.flag_team(1)

        #team/spieler sammeln
        elif str(message.channel) == "bot"  and funktion.flag_team(2) == 1:
            log.write_log("entered the team selection",message.author)
            funktion.add_user(message.author,message.content)

        #random
        if message.content.startswith("bot random"):
            log.write_log("random number",message.author)
            await message.channel.send("First Number")
            funktion.flag_random(1)
        elif funktion.flag_random(2) == 1:
            global erste_zahl
            erste_zahl = int(message.content)
            await message.channel.send("Second number")
            funktion.flag_random(3)
        elif funktion.flag_random(2) == 3:
            zweite_zahl = int(message.content)
            zahl = random.randint(erste_zahl,zweite_zahl)
            await message.channel.send("Your number is: " + str(zahl))

        #würfel
        if message.content.startswith("bot dice"):
            text = str(message.content)
            text_zahl = []
            zahl = 0
            if text == "bot dice":
                zahl = 6
            for i in range(len(text)):
                try:
                    int(text[i])
                    text_zahl = text_zahl + [str(text[i])]
                except ValueError:
                    None

            text_zahl.reverse()
            multiplikator = [1, 10, 100, 1000, 10000, 100000, 1000000]

            for i in range(len(text_zahl)):
                zahl = zahl + int(text_zahl[i]) * multiplikator[i]
            zahl = random.randint(1,zahl)
            await message.channel.send("The dice says: " + str(zahl))

        #münze
        if message.content.startswith("bot coin") or message.content.startswith("bot toss"):
            zahl = random.randint(1,2)
            if zahl == 1:
                await message.channel.send("Kopf")
            if zahl == 2:
                await message.channel.send("Zahl")
            if message.content.startswith("bot toss"):
                await message.channel.send("toss a coin to your witcher")






client = MyClient()
client.run("token")

