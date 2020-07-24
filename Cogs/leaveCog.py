import discord
from discord.ext import commands
import asyncio
import datetime

class leaveCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='leave')
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.message.delete()
def setup(bot):
    bot.add_cog(leaveCog(bot)) 