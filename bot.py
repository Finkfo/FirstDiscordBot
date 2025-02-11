import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from config import TOKEN
import events
import commands_list

# Chargement des variables d'environnement
load_dotenv()

print("Lancement du bot...")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Importer les événements
events.setup(bot)

# Importer les commandes
commands_list.setup(bot)

# Démarrage du bot
bot.run(TOKEN)