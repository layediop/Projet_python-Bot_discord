import os
import discord
from discord.ext import commands
client = commands.Bot(command_prefix="$")
class Node :
    def __init__(self,question,keyword,list_child_node):
        self.question = question
        self.keyword = keyword
        self.list_child_node = list_child_node

    def user_response(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node:
            if child.keyword in txt:
                child.user_response()

first_node =Node("Bonjour!\nGuide : Comment je fonctionne?\nNous n'avons que 2 types de langages à vous proposer(php et python) et uniquement pour les debutants\nJe dirige la discussion et je repère les mots clèfs pour répondre à vos questions.\nLes commandes possibles : \n$help -> démarrer une nouvelle discussion.\nreturn -> retouner en arrière.\nAvez vous besoin d'un cours?", "help",
[Node("Quel type de langage ?", "cours",
[Node("Voulez vous des tutos ?", "php",
[Node("Avez vous un niveau debutant ?", "tutos",
[Node("Avez vous des problemes en php ?", "debutant",
[Node("Je vous conseille de suivre ce tuto:(https://www.youtube.com/watch?v=FKdctsQ1v7U&t=1s) ça vous vas?", "problemes",
[Node("Voulez vous d'une documentation pour ça ?", "oui",
[Node("Cette documentation est faite pour vous:(https://www.php.net/), avez vous besoin de documentation en python ?","oui", 
[Node("Cette documentation est faite pour vous:(https://docs.python.org/fr/3/reference/index.html)", "oui",[])])])])])])]),Node("Voulez vous des tutos ?","python",
[Node("Peut on savoir si vous avez un niveau debutant ?", "tutos", 
[Node("je vous suggere ce tuto:(https://www.youtube.com/watch?v=oUJolR5bX6g&t=2439s) ça vous vas ?", "debutant", 
[Node("Voulez vous d'une documentation ?", "oui", 
[Node("Je vous invite à aller suivre ce site:(https://docs.python.org/fr/3/tutorial/)", "documentation",
[])])])])])])])
current_node = first_node


default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Je suis connecté")

@client.event
async def on_message(message):
    if message.content.startswith("return"):
        await message.channel.purge(limit=2)
    
        message.content = message.content.lower()
    if message.author == client.user:
        return
    Help_channel = client.get_channel(980736173855100951)
    global current_node

    if message.channel == Help_channel and message.content =='$help':
        await Help_channel.send("@"+message.author.name)
        await Help_channel.send(first_node.question)

    for child in current_node.list_child_node:
        if child.keyword in message.content:
            await Help_channel.send(child.question)
            current_node = child    
@client.event
async def on_member_join(member):
    general_channel = client.get_channel(909903148028670036)
    await general_channel.send(content=f"Bienvenue sur notre serveur {member.display_name} !")    



client.run("OTgwNzM0Mjc1NzgxNTM3ODc0.GxDHNX.G3IsV5bBU4oWYFdxzV9FgHRsV6ShSknETrCPmw")
