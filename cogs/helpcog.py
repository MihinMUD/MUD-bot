import discord
from discord.ext import commands


class helpcog(commands.Cog):
    def __init__(self, client , command = "" , descp = "" ):
        self.client = client
        self.command = command
        self.descp = descp

    @commands.command()
    async def about(self , ctx):
        about_embed = discord.Embed(
            title="About me..",
            description="I was created by <@!756868676040392784> ",
            colour=discord.Colour.blue()
        )
        about_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/756868676040392784/a2b1b50d8ffd88954da401769b092c36.png?size=256")
        about_embed.add_field(name="What can i do?", value="I'm a just friendly, fun chat bot! :)", inline=False)
        about_embed.add_field(name="How to use me?", value="Type 'mud help'", inline=False)
        about_embed.set_author(name="MihinMUD",
                            icon_url="https://cdn.discordapp.com/avatars/756868676040392784/a2b1b50d8ffd88954da401769b092c36.png?size=256")
        await ctx.send(embed=about_embed)

def setup(client):
    client.add_cog(helpcog(client))