import discord
from discord.ext import commands

TOKEN = 'Njk3OTc0NDI1MDcyNTY2Mjkz.Xs09Wg.OdaArzhePDbUTtsG5hwbAOuZPp4'
bot = commands.Bot(command_prefix = "-")

extensions = ['RolechangeCog', 'SayEmbedCog', 'SayEmbedCogeveryone']

#Events 
@bot.event
async def on_ready():
    print('Bot Online.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("BHF Event"))

#Commands 

@bot.command()
async def load(extension):
    try:
        bot.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded [{}]'.format(extension, error))

@bot.command()
async def unload(extension):
    try:
        bot.unload_extension(extension)
        print('unLoaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded [{}]'.format(extension, error))


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension, error))
    bot.run(TOKEN)