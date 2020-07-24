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
            description='The prefix for the bot is ``bhf.`` \n \n ``info`` - Shows some event information! \n ``help`` - Shows this screen! Shows what commands you can use! \n ``join`` - Joins the voice channel you are currently in. \n ``tfm`` - Plays TruckersFM! \n ``capital`` - Plays CapitalFM! \n ``leave`` - Leaves the current voice channel. \n  \n Bot is a work in progress, more commands will be added (:',
            title='Help!')

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        await ctx.channel.send(embed=embed)
            

        await ctx.message.delete()
def setup(bot):
    bot.add_cog(helpCog(bot)) 