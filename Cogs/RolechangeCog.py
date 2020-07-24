import discord
from discord.ext import commands
import asyncio
import datetime

class SayEmbedCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='rolechange')
    @commands.has_any_role("Event Founder", "Event Organiser", "Event Supervisor", "Media Manager", "Streamer Manager")
    async def say_embed(self, ctx, *, message):
        channel = self.bot.get_channel(678328684750307328)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            description=message
        )
        embed.set_author(name='Member Change',
                         icon_url=self.bot.user.avatar_url)
        #embed.add_field(name='\u200b', value=message, inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'Posted by {ctx.message.author.name}',
                         icon_url=ctx.message.author.avatar_url)

        if ctx.message.attachments:
            f = await ctx.message.attachments[0].to_file()
            embed.set_image(url=f"attachment://{f.filename}")
            await channel.send(file=f, embed=embed)

        else:
            await channel.send(embed=embed)

        await ctx.message.delete()
def setup(bot):
    bot.add_cog(SayEmbedCog(bot))