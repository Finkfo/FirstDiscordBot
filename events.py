import discord

def setup(bot):
    @bot.event
    async def on_ready():
        print("Bot prêt !")
        try:
            synced = await bot.tree.sync()
            print(f"Commandes slash synchronisées : {len(synced)}")
        except Exception as e:
            print(e)

    @bot.event
    async def on_message(message: discord.Message):
        if message.author.bot:
            return

        if message.content.lower() == 'bonjour':
            await message.author.send("Molenbeek !")
            await message.channel.send("https://tenor.com/view/powder-ekko-plume-powder-ekko-plumaximus-arcane-gif-17589169359600433832")

        if message.content.lower() == "bienvenue":
            welcome_channel = bot.get_channel(1337014670774763543)
            await welcome_channel.send("https://tenor.com/view/jinx-arcane-season-2-gif-8431263884746412975")