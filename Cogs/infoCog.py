import discord
from discord.ext import commands
import asyncio
import datetime

class infoCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='info')
    async def say_embed(self, ctx):
        embed = discord.Embed(
            title = 'Event Information',
            colour=discord.Colour.red(),
            description='**Date** - 25th July 2020 \n **Meetup Time** - 11:45 BST \n **Meetup Time** - 11:45 BST \n **Truckfest** - 12:00 BST \n **Judging** - 12:35 BST \n **Collect Trailer** - 12:45 BST \n **Departure** - 13:00 BST \n \n **Route 1** - Frankfurt - Dover \n **Route 2** - Dover - Amsterdam \n **Route 3** - Amsterdam - Szczecin \n **Route 4** - Szczecin - Kosice \n **Route 5** - Kosice - Brasov \n **Route 6** - Brazov - Pirdop \n \n **How to find us** \n \n **ETS2c** - https://ets2c.com/view/84872/vexus-frankfurt-hotel \n **Discord** - https://discord.gg/2FfGSXa \n **Forum** - https://forum.truckersmp.com/index.php?/topic/93188-25th-july-2020-the-bhf-event/'
        )

        embed.set_footer(text='BHF Event', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url="https://images.nathan7471.xyz/q705a9sm.jpg")

        await ctx.channel.send(embed=embed)
        await ctx.message.delete()
def setup(bot):
    bot.add_cog(infoCog(bot))