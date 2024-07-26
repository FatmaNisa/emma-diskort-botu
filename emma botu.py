import discord
from discord.ext import commands
import emmakod

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    
@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum! benden hangi konuda yardım istiyorsun çevre yada meslek (hangisini istiyorsan $ la onu yaz)')
@bot.command()
async def çevre(ctx):
    await ctx.send(emmakod.cevrekod())
@bot.command()
async def meslek(ctx):
    await ctx.send(emmakod.meslekler())


bot.run("MTI1ODgyNjU2NDA4MzEyMjMwOA.GtoOFo.wXLJYGq3yLJojaaMIHRqfnkAbyv38xtObMOdkA")