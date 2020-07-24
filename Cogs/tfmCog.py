import discord
from discord.ext import commands
import asyncio
import datetime
import ffmpeg

class joinCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='tfm')
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await ctx.message.delete()
        print(f"{ctx.message.author.name} ran join and play tfm.```")
        vc.play(discord.FFmpegPCMAudio('http://live.truckers.fm'))
def setup(bot):
    bot.add_cog(joinCog(bot)) 