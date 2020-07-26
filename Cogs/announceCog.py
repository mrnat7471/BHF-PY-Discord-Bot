import discord
from discord.ext import commands, tasks
import asyncio
import datetime
import json
import requests
import time
from itertools import cycle

class announceCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name="announce")
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def announce(self, ctx, *, message):
        channel = self.bot.get_channel(591923276855509006)
        embed = discord.Embed(
                colour=discord.Colour.red(),
                description=message,
                title='BHF Announcement'
            )
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        if ctx.message.attachments:
            f = await ctx.message.attachments[0].to_file()
            embed.set_image(url=f"attachment://{f.filename}")
            await channel.send(file=f, embed=embed)

        else:
            await channel.send(embed=embed)
                

        await ctx.message.delete()

    @bot.command(name="announce-cc")
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def cc(self, ctx, *, message):
        channel = self.bot.get_channel(665965794538029065)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            description=message,
            title='BHF CC Announcement'
        )
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        if ctx.message.attachments:
            f = await ctx.message.attachments[0].to_file()
            embed.set_image(url=f"attachment://{f.filename}")
            await channel.send("<@&587223671899422731>")
            await channel.send(file=f, embed=embed)

        else:
            await channel.send("<@&587223671899422731>")
            await channel.send(embed=embed)
            

        await ctx.message.delete()

    @bot.command(name="announce-everyone")
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def everyone(self, ctx, *, message):
        channel = self.bot.get_channel(591923276855509006)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            description=message,
            title='BHF Announcement'
        )
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        if ctx.message.attachments:
            f = await ctx.message.attachments[0].to_file()
            embed.set_image(url=f"attachment://{f.filename}")
            await channel.send("@everyone")
            await channel.send(file=f, embed=embed)

        else:
            await channel.send("@everyone")
            await channel.send(embed=embed)
            

        await ctx.message.delete()

    @bot.command(name="announce-here")
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def here(self, ctx, *, message):
        channel = self.bot.get_channel(591923276855509006)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            description=message,
            title='BHF Announcement'
        )
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        if ctx.message.attachments:
            f = await ctx.message.attachments[0].to_file()
            embed.set_image(url=f"attachment://{f.filename}")
            await channel.send("@here")
            await channel.send(file=f, embed=embed)

        else:
            await channel.send("@here")
            await channel.send(embed=embed)
            

        await ctx.message.delete()

    @bot.command(name="announce-media")
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def media(self, ctx, *, message):
        channel = self.bot.get_channel(604860924163260416)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            description=message,
            title='BHF Media Announcement'
        )
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        if ctx.message.attachments:
            f = await ctx.message.attachments[0].to_file()
            embed.set_image(url=f"attachment://{f.filename}")
            await channel.send("<@&587223841370013698>")
            await channel.send(file=f, embed=embed)

        else:
            await channel.send("<@&587223841370013698>")
            await channel.send(embed=embed)
            

        await ctx.message.delete()

    @bot.command(name="announce-staff")
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def staff(self, ctx, *, message):
        channel = self.bot.get_channel(678756103651328010)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            description=message,
            title='BHF Staff Announcement'
        )
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        if ctx.message.attachments:
            f = await ctx.message.attachments[0].to_file()
            embed.set_image(url=f"attachment://{f.filename}")
            await channel.send("<@&678755714663186463>")
            await channel.send(file=f, embed=embed)

        else:
            await channel.send("<@&678755714663186463>")
            await channel.send(embed=embed)
            

        await ctx.message.delete()
def setup(bot):
    bot.add_cog(announceCog(bot))