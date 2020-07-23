import discord
import random

class MyClient(discord.Client):
    #einlogen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep bop.")

    #wenn nachricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content == "$help":
            await message.channel.send("Für Roulette: $roulette BID eingeben, wobei BID = black \n"
                                       " red \n number")

        if message.content.startswith("$roulette"):
            bid = message.content.split(" ")[1]
            bif_param =  -3
            if bid.lower() == "black":
                bif_param = -1
            if bid.lower() == "red":
                bif_param = -2
            else:
                try:
                    bif_param = int(bid)
                except:
                    bif_param = -3
            if bif_param == -3:
                await message.channel.send("Fehler")
                return
            result = random.randint(0,36)
            print(result)
            if bif_param == -1:
                won = result%2 == 0 and not result == 0
            elif bif_param == -2:
                won = result%2 == 1
            else:
                won = result == bif_param
            if won:
                await message.channel.send("$$$ Du hast gewonnen")
            else:
                await  message.channel.send("You suck ")


client = MyClient()
client.run("NzEzNzQxMTI0NzAzMDkyNzQ2.Xskhiw.y-tNpqTYVcwS1nsbIrXUn1J0QAY")