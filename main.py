import discord
from discord.ext import commands
import sys


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
    await ctx.send('Hello comrade! I am PravdaAgendaBot, made by my glorius leader ``pengu211`` and great contributer ``mattphantastic``\n# Commands\n```!agenda createAgenda\n[-title]\n[-timestamp]\n[-invite]\n[-agenda]```')

@bot.command()
async def createAgenda(ctx, *, input):
    channel = bot.get_channel(1138848822727032963)
    # The arguments:
    args = {'dummy': ''}
    # Read line by line:
    lines = input.split('\n')
    for line in lines:
        words = line.split(' ')
        param = words[0]  # First word of line
        # New parameters start with dashes:
        if param[0] == '-':
            value = ' '.join(words[1:])  # Rest of line
            args[param] = value
        else:  # Does not start with dash?
            args['dummy'] += f'\n{line}'  # Append the whole line
    # Assemble output:
    output = '#'
    if '-timestamp' in args:
        output += f' {args["-timestamp"]}'
    if '-title' in args:
        output += f' Meeting: {args["-title"]}'
        thread = await channel.create_thread(name=args['-title'])
    else:
        await ctx.send('Please type a title in.')
    if '-agenda' in args:
        output += f'\n{args["-agenda"]}'
    if '-invite' in args:
        output += f'\n\nInvited: {args["-invite"]} {ctx.author.mention}'
    
    await thread.send(output)
    await ctx.send(output)


# @bot.command()
# async def add(ctx, arg1, arg2, *, arg3):
#     await ctx.send(f'New Agenda made:\n# {arg1}\n{arg3}')
#     channel = bot.get_channel(1138848822727032963)
#     thread = await channel.create_thread(name=arg1)
#     await thread.send(f'# {arg1}\n{arg3}')
#     await thread.send(ctx.author.mention)
#     await thread.send(arg2)


bot.run('no token for u')