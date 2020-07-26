import discord
from discord.ext import commands
import asyncio
import datetime

class helpCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')
    bot.remove_command('help')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='help')
    async def help(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.red(), 
            description="""The prefix for the bot is ``bhf.``
            
            ``info`` - Shows some event information!
            ``help`` - Shows this screen! Shows what commands you can use!
            ``play tfm`` - Plays TruckersFM!
            ``play capital`` - Plays CapitalFM!
            ``leave`` - Leaves the current voice channel.""",
            title='Help!')

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        await ctx.channel.send(embed=embed)
            

        await ctx.message.delete()
def setup(bot):
    bot.add_cog(helpCog(bot)) 