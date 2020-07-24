import discord
from discord.ext import commands
import asyncio
import datetime

class donationsCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='donation')
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def say_embed(self, ctx, *, message):
        channel = self.bot.get_channel(659922517141749760)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            description=message,
            title='Donation'
        )
        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()

        if ctx.message.attachments:
            f = await ctx.message.attachments[0].to_file()
            embed.set_image(url=f"attachment://{f.filename}")
            await channel.send(file=f, embed=embed)

        else:
            await channel.send(embed=embed)
            

        await ctx.message.delete()
def setup(bot):
    bot.add_cog(donationsCog(bot))