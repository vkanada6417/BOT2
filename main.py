import discord
from discord.ext import commands
from time import sleep
from funk import *

help_info = [
    "Советы по тому как стать экологичнее: $-how_to_eco  ",
    'Сколько что разлогается: $-whenraz  ',
    "Список команд: $-com_help  ",
    "Спам: $-spam 'сколько раз'  ",
    "Рандомный миф про экологию: $-eco_mith  "
]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$-', intents=intents)



@bot.command()
async def how_to_eco(ctx):
    await ctx.send(f"{random_fact()}")

@bot.command()
async def eco_mith(ctx):
    await ctx.send(f"{eko_mith()}")

@bot.command()
async def whenraz(ctx):
    await ctx.send(f"{raz_log()}")

        
@bot.command()
async def com_help(ctx):
    for i in help_info:
        await ctx.send(i)


@bot.command()
async def spam(ctx, spam_count=10):
    for i in range(spam_count):
        await ctx.send(f"Spam Spam Spam {i+1}")
        

bot.run("")