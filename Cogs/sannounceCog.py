import discord
from discord.ext import commands
import asyncio
import datetime

class sannounceCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='sannounce')
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def say_embed(self, ctx, *, message):
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
    bot.add_cog(sannounceCog(bot))