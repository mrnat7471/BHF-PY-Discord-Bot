import discord
from discord.ext import commands
import asyncio
import datetime

class helpCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='adminhelp')
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def help(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.red(), 
            description='The prefix for the bot is ``bhf.`` \n \n ``announce`` = Sends an Announcement to the Announcements Channel \n ``ccannounce`` = Sends an CC announcement \n ``donation`` = Sends Donation to Donation Channel \n ``everyone`` = Sends an Everyone Announcement \n ``mannounce`` = Sends an Media Announcement \n ``purge`` = Purge X Messages \n ``recruit`` = Send a recruit message to recruit channel \n ``rolechange`` = Send a role change announcement \n ``route`` = Send a new route (Message is embed title) \n ``sannounce`` = Staff Announcement \n ``testannounce`` = Embed Message \n ``testeveryone`` = Everyone Ping Embed Message \n ``slots`` = Sends a slot photo embed to slot channel (message = Title)',
            title='Admin Help!')

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        await ctx.channel.send(embed=embed)
            

        await ctx.message.delete()
def setup(bot):
    bot.add_cog(helpCog(bot)) 