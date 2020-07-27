import discord
from discord.ext import commands
import asyncio
import datetime
import ffmpeg

class playCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def play(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(colour=discord.Colour.red(), description="Please do bhf.play (tfm, capital or sr or (reach - Nathan7471 can't only run this command till radio release)")
            embed.set_author(name='BHF Bot', icon_url=self.bot.user.avatar_url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'BHF Bot Radio Module', icon_url=self.bot.user.avatar_url)

            message = await ctx.channel.send(embed=embed)

    @play.command()
    async def tfm(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await ctx.message.delete()
        print(f"{ctx.message.author.name} ran join and play tfm.")
        vc.play(discord.FFmpegPCMAudio('http://djs.truckers.fm:8010/live'))

        embed = discord.Embed(colour=discord.Colour.red(), description="Join your voice channel & now playing TruckersFM")
        embed.set_author(name='BHF Bot', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'BHF Bot Radio Module', icon_url=self.bot.user.avatar_url)

        message = await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @play.command()
    async def capital(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await ctx.message.delete()
        print(f"{ctx.message.author.name} ran join and play capital.")
        vc.play(discord.FFmpegPCMAudio('http://media-ice.musicradio.com/CapitalMP3'))

        embed = discord.Embed(colour=discord.Colour.red(), description="Join your voice channel & now playing Capital Radio London")
        embed.set_author(name='BHF Bot', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'BHF Bot Radio Module', icon_url=self.bot.user.avatar_url)

        message = await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @play.command()
    async def sr(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await ctx.message.delete()
        print(f"{ctx.message.author.name} ran join and play SR")
        vc.play(discord.FFmpegPCMAudio('https://simulatorradio.stream/96'))

        embed = discord.Embed(colour=discord.Colour.red(), description="Join your voice channel & now playing Simulator Radio")
        embed.set_author(name='BHF Bot', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'BHF Bot Radio Module', icon_url=self.bot.user.avatar_url)

        message = await ctx.channel.send(embed=embed)
        await ctx.message.delete()
        
    @play.command()
    async def tsr(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await ctx.message.delete()
        print(f"{ctx.message.author.name} ran join and play truckstopradio")
        vc.play(discord.FFmpegPCMAudio('https://truckstopradio.radioca.st/stream.mp3'))

        embed = discord.Embed(colour=discord.Colour.red(), description="Join your voice channel & now playing truckstopradio")
        embed.set_author(name='BHF Bot', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'BHF Bot Radio Module', icon_url=self.bot.user.avatar_url)

        message = await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @play.command()
    @commands.is_owner()
    async def reach(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await ctx.message.delete()
        vc.play(discord.FFmpegPCMAudio('https://stream.reachradio.co.uk'))
def setup(bot):
    bot.add_cog(playCog(bot)) 