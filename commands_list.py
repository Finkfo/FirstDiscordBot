import discord

def setup(bot):
    @bot.tree.command(name="help", description="Affiche la liste des commandes")
    async def help(interaction: discord.Interaction):
        embed_help = discord.Embed(
            title="Liste des commandes",
            description="Voici la liste des commandes disponibles",
            color=discord.Color.red()
        )
        embed_help.add_field(name="powder", value="Affiche le Wiki de Powder (Jinx)", inline=False)
        embed_help.add_field(name="charleroi", value="Charleroi la personne de ton choix", inline=False)
        embed_help.add_field(name="banguy", value="Bannis la personne de ton choix", inline=False)
        embed_help.set_image(url="https://media.discordapp.net/attachments/1337434499159691294/1337434515538313347/s2-act-3-spoilers-pomme-powder-v0-c9orvvtk0y2e1.png")
        embed_help.set_footer(text="Bot créé par FinkSo")
        await interaction.response.send_message(embed=embed_help)

    @bot.tree.command(name="powder", description="Affiche le Wiki de Powder (Jinx)")
    async def powder(interaction: discord.Interaction):
        await interaction.response.send_message("Voici le Wiki de Powder : https://arcane.fandom.com/wiki/Jinx")

    @bot.tree.command(name="charleroi", description="Charleroi la personne de ton choix")
    async def charleroi(interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message("Charleroi envoyé à " + member.mention)
        await member.send("Tu es aussi beau que Charleroi, Bisous !")

    @bot.tree.command(name="banguy", description="Bannis la personne de ton choix")
    async def banguy(interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message("Ban envoyé à " + member.mention + " !")
        await member.send("Tu as été banni du serveur car tu n'es pas aussi beau que Charleroi")
        await member.ban(reason="Désolé tu n'est pas aussi beau que Charleroi")
