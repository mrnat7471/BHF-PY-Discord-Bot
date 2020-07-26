import discord
from discord.ext import commands
import ffmpeg
import asyncio
import datetime

TOKEN = 'NjA4NjYzMjM2MjM3MzI4Mzg2.XqHB4A.N-NGZ585F9WvJPCgZLj1ZmIbMgI'
bot = commands.Bot(command_prefix = "bhf.", owner_id=510238066829688832) 
bot.remove_command('help')

extensions = ['adminCog', 
'announceCog', 
'tfmurlCog', 
'donationsCog', 
'helpCog', 
'infoCog', 
'leaveCog', 
'purgeCog', 
'RecruitCog', 
'RolechangeCog', 
'RouteCog',  
'SayEmbedCog', 
'SayEmbedCogeveryone', 
'slotsCog', 
'playCog']

#Event
@bot.event
async def on_ready():
    print('Bot Online.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='BHF Discord'))

@bot.event
async def on_command_error(ctx, error):
    print(str(error))
    ignored = (commands.CommandNotFound, commands.UserInputError)
    if isinstance(error, ignored):
        return

    if isinstance(error, commands.CommandOnCooldown):
        m, s = divmod(error.retry_after, 60)
        h, m = divmod(m, 60)
        if int(h) == 0 and int(m) == 0:
            await ctx.channel.send(f'You must wait {int(s)} seconds to use this command!')
        elif int(h) == 0 and int(m) != 0:
            await ctx.channel.send(f'You must wait {int(s)} minutes and {int(s)} seconds to use this command!')
        else:
            await ctx.channel.send(f'You must wait {int(h)} hours, {int(s)} minutes and {int(s)} seconds to use this command!')
    elif isinstance(error, commands.CheckFailure):
        await ctx.channel.send("You lack permission to use this command.")
        raise error

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

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension("Cogs." + extension)
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension, error))
    bot.run(TOKEN)