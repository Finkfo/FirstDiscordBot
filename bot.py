import discord  # Importation de la librairie discord.py
import os  # Importation de la librairie os
from dotenv import load_dotenv  # Importation de la librairie python-dotenv
from discord.ext import commands # Importation de la classe commands de la librairie discord.py
load_dotenv()

print("Lancement du bot...")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())  # Création du bot avec le préfixe "!"



@bot.event  # Décorateur pour indiquer que la fonction est un événement
async def on_ready():  # Fonction appelée lorsque le bot est prêt
    print("Bot prêt !")  # Affichage d'un message dans la console

    #Synchronisation des commandes slash
    try: # Essayer de synchroniser les commandes slash
        synced = await bot.tree.sync() # Synchronisation des commandes slash
        print(f"Commandes slash synchronisées : {len(synced)}") # Affichage du nombre de commandes synchronisées dans la console
    except Exception as e: # Si une erreur se produit
        print(e) # Affichage de l'erreur dans la console



@bot.event  # Décorateur pour indiquer que la fonction est un événement
async def on_message(message: discord.Message):  # Fonction appelée lorsqu'un message est envoyé
    if message.author.bot:  # Si l'auteur du message est un bot
        return  # Arrêt de la fonction

    if message.content.lower() == 'bonjour': # Si le contenu du message est "bonjour"
        channel = message.channel # Récupération du salon où le message a été envoyé
        author = message.author # Récupération de l'auteur du message
        await author.send("Molenbeek !") # Envoi d'un message privé à l'auteur
        await channel.send("https://tenor.com/view/powder-ekko-plume-powder-ekko-plumaximus-arcane-gif-17589169359600433832") # Envoi d'un message dans le salon

    if message.content.lower() == "bienvenue" : # Si le contenu du message est "bienvenue"
        welcome_channel = bot.get_channel(1337014670774763543) # Récupération du salon de bienvenue
        await welcome_channel.send("https://tenor.com/view/jinx-arcane-season-2-gif-8431263884746412975") # Envoi d'un message dans le salon de bienvenue



@bot.tree.command(name="help", description="Affiche la liste des commandes")  # Décorateur pour indiquer que la fonction est une commande
async def help(interaction: discord.Interaction): 
    embed_help=discord.Embed( # Création d'un embed pour afficher la liste des commandes
        title="Liste des commandes", # Titre de l'embed
        description="Voici la liste des commandes disponibles", # Description de l'embed
        color=discord.Color.red() # Couleur de l'embed
    )
    embed_help.add_field(name="powder", value="Affiche le Wiki de Powder (Jinx)", inline=False) # Ajout d'un champ pour la commande "powder"
    embed_help.add_field(name="charleroi", value="Charleroi la personne de ton choix", inline=False) # Ajout d'un champ pour la commande "charleroi"
    embed_help.add_field(name="banguy", value="Bannis la personne de ton choix", inline=False) # Ajout d'un champ pour la commande "banguy"

    embed_help.set_image(url="https://media.discordapp.net/attachments/1337434499159691294/1337434515538313347/s2-act-3-spoilers-pomme-powder-v0-c9orvvtk0y2e1.png?ex=67a76e74&is=67a61cf4&hm=523109f06051933357cc0414f530a69d8a2148180bc9e406f99688ba7e04b2bb&=&format=webp&quality=lossless&width=350&height=350") # Ajout d'une image à l'embed
    embed_help.set_footer(text="Bot créé par FinkSo") # Ajout d'un footer à l'embed
    await interaction.response.send_message(embed=embed_help) # Envoi d'un message contenant la liste des commandes

@bot.tree.command(name="powder", description="Affiche le Wiki de Powder (Jinx)")  # Décorateur pour indiquer que la fonction est une commande
async def powder(interaction: discord.Interaction): # Fonction appelée lorsqu'un utilisateur interagit avec la commande
    await interaction.response.send_message("Voici le Wiki de Powder : https://arcane.fandom.com/wiki/Jinx") # Envoi d'un message contenant le lien du Wiki de Powder

@bot.tree.command(name="charleroi", description="Charleroi la personne de ton choix") # Décorateur pour indiquer que la fonction est une commande
async def molenbeek(interaction: discord.Interaction, member: discord.Member): # Fonction appelée lorsqu'un utilisateur interagit avec la commande
    await interaction.response.send_message("Charleroi envoyé à " + member.mention) # Confirmation de l'envoi de Charleroi à l'utilisateur
    await member.send("Tu es aussi beau que Charleroi, Bisous !") # Envoi d'un message privé à l'utilisateur

@bot.tree.command(name="banguy", description="Bannis la personne de ton choix") # Décorateur pour indiquer que la fonction est une commande
async def banguy(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message("Ban envoyé à " + member.mention + " !") # Confirmation de l'envoi du ban à l'utilisateur
    await member.send("Tu as été banni du serveur car tu n'es pas aussi beau que Charleroi") # Envoi d'un message privé à l'utilisateur
    await member.ban(reason="Désolé tu n'est pas aussi beau que Charleroi") # Ban de l'utilisateur
    


bot.run(os.getenv('DISCORD_TOKEN'))  # Connexion du bot avec le token