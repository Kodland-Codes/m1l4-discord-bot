import discord
from discord.ext import commands

# Discord botunun Discord sunucusuna mesaj atmasi icin izinleri acmamiz gerekiyor.
intents = discord.Intents.default()
intents.message_content = True

#Botumu olusturuyoruz
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
    
@bot.command()
async def kodland(ctx):
    await ctx.send(f'Kodlanda {bot.user}! hoşgeldiniz')

@bot.command()
async def name(ctx):
    await ctx.send(f'Merhaba, benim ismim Kuzey')
    
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("Selim" * count_heh)

bot.run("TOKEN")
