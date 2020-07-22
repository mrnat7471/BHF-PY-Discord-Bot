import discord
from discord.ext import commands
import ffmpeg
import asyncio
import datetime

TOKEN = 'NjA4NjYzMjM2MjM3MzI4Mzg2.XqHB4A.N-NGZ585F9WvJPCgZLj1ZmIbMgI'
bot = commands.Bot(command_prefix = "bhf.") 
bot.remove_command('help')

extensions = ['adminCog', 'announceCog', 'CapitalCog', 'tfmurlCog', 'ccannounceCog', 'donationsCog', 'everyoneCog', 'helpCog', 'infoCog', 'leaveCog', 'mannounceCog', 'purgeCog', 'RecruitCog', 'RolechangeCog', 'RouteCog', 'sannounceCog', 'SayEmbedCog', 'SayEmbedCogeveryone', 'slotsCog', 'tfmCog']

#Event
@bot.event
async def on_ready(self, bot):
    self.bot = bot
    print('Bot Online.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=len(bot.guild.members)))

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    role = discord.utils.get(member.guild.roles, name="Public")
    embed = discord.Embed(colour=discord.Colour.red(), description=f"Welcome to the BHF Event Discord server, {member.mention}! \n \n > 💕 Head over to <#587224128516390913> to read our rules! \n > 💕 Head over to <#587224234384949258> to see information on our next event! \n > 💕 Head over to <#591923276855509006> to see any announcements regarding our events! \n \n We hope you enjoy your stay in our discord server!",
    title='Welcome!')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")  
    await channel.send(embed=embed)
    await member.add_roles(role)
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