import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!agenda ', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!agenda commands || Pengu"))
    
# @bot.command()
# async def channel(ctx, arg):
#     cha = await ctx.guild.create_text_channel(arg)
@ bot.command()
async def commands(ctx):
    await ctx.send('Hello comrade! I am PravdaAgendaBot, made by my glorius leader ``pengu211``\n# Commands\n```!agenda add [The title of the agenda] [Metion people or roles here] [Discription of the agenda]```')


@bot.command()
async def add(ctx, arg1, arg2, *, arg3):
    await ctx.send(f'New Agenda made:\n# {arg1}\n{arg3}')
    channel = bot.get_channel(1138848822727032963)
    thread = await channel.create_thread(name=arg1)
    await thread.send(f'# {arg1}\n{arg3}')
    await thread.send(ctx.author.mention)
    await thread.send(arg2)


bot.run()