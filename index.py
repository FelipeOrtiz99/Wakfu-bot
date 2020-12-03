import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!',description='Wakfu bot')


@bot.command()
async def b(ctx, *, search):
    url =  'https://www.wakfu.com/es/mmorpg/enciclopedia/monstruos?text='
    url_search = url + search

    await ctx.send(url_search)

@bot.command()
async def guide(ctx):
    await ctx.send('https://www.wakfu.com/es/foro/200-hipermagos/148393-guia-owejeras-hipermago-2020')


bot.run('Nzg0MTIwMTUzNzEzMjc4OTc2.X8kqzA.2XTG_Dt23k1g9bPLpR87r-b0NDw')


