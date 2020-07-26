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
            description="""
            The prefix for the bot is ``bhf.``
            
            ``announce`` = Sends an Announcement to the Announcements Channel
            ``announce-cc`` = Sends an CC announcement
            ``donation`` = Sends Donation to Donation Channel
            ``announce-everyone`` = Sends an Everyone Announcement
            ``announce-media`` = Sends an Media Announcement
            ``purge`` = Purge X Messages
            ``recruit`` = Send a recruit message to recruit channel
            ``rolechange`` = Send a role change announcement
            ``route`` = Send a new route (Message is embed title)
            ``announce-staff`` = Staff Announcement
            ``testannounce`` = Embed Message
            ``testeveryone`` = Everyone Ping Embed Message
            ``slots`` = Sends a slot photo embed to slot channel (message = Title)""",
            title='Admin Help!')

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        await ctx.channel.send(embed=embed)
            

        await ctx.message.delete()
def setup(bot):
    bot.add_cog(helpCog(bot)) 