# Sur discord passer en mode developpeur 
# Sur le portail developpeur discord créer une app
# Créer un bot sur cette Application
#bot token OTc2Nzg1MDYwMDU5NTc4Mzcw.GkDkZH.V2euT1BS54qSikNJp6ZQURrpzOUDI1xD_bFUHM
#auth token 0zkX64sFG-6yighZRmXdDBQ37YAli-3w

#pour verifier les utilisateurs il faut activer sur le dashboard admin : 
# - 

import discord
import os

from discord.ext import commands

client = discord.Client()

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(621791536916725779) #id a trouver quand on passe en mode dev sur discord
    member.send("L'utilisateur",member.display_name,"a rejoint le serveur !")

@client.event
async def on_ready():
    print('We have logged in')

@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return

    texte_channel = client.get_channel(977137496720826368)

    if message.content.startswith("$dm"): 
        user = message.mentions[0]
        strs = message.content.split(" ")
        await user.send(strs[2:])


    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        #await texte_channel.send("Hello")

    image_channel = client.get_channel(977135029614432296)
    if message.channel == image_channel and message.content != "":
        await message.channel.purge(limit=1)

client.run("OTc4MjI5MzAzMTQzNzAyNTU4.Gjc-UJ.rLGYRku77ZVXje38908-x5OQDH4sjK99WUCUA0")