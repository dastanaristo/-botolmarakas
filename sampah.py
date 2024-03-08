import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def botolmarakas(ctx):
    messages = [
        "Isilah setengah botol plastik berukuran 250 mililiter dengan bahan-bahan yang dapat menghasilkan bunyi berisik",
        "Pasang salah satu bukaan (ujung) tabung pada leher botol dan kencangkan tabung sehingga rapat dengan leher botol",
        "Gunakan pita perekat untuk mengunci tabung karton dengan botol",
        "Balut seluruh bagian tabung karton dengan pita perekat tambahan",
        "Setelah selesai, buatlah marakas kedua",
        "Mainkan marakas Anda"
    ]

    for i in range(6):
        with open(f'images/M{i+1}.jpeg', 'rb') as file:
            picture = discord.File(file)
            await ctx.send(messages[i], file=picture)  # Send a different message for each image

bot.run('SUGNOMA')
