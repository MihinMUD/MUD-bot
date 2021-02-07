import discord
from discord.ext import commands
import urllib.parse, urllib.request, re
from pyfiglet import Figlet
import random

LUCK_SPIN=[
    "Head",
    "Tail"
]

f = Figlet(font='slant')


def choose_word(string):
    list_of_words = string.split()
    return f"MyChoice is: ***{random.choice(list_of_words)}***"

def get_youtube_data(term):
    query_string = urllib.parse.urlencode({'search_query': term})
    htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    return 'http://www.youtube.com/watch?v=' + search_results[0]


class featurescog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def leave(self , ctx):
        await ctx.send("I am leaving this guild!")
        await ctx.guild.leave()

    @commands.command()
    async def figlet(self , ctx , *,words):
        if len(words) <= 40:
            await ctx.send(f"```{f.renderText(words)}```")
        else:
            await ctx.send(f":face_palm: Sentence is Too Long!")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clr(self , ctx, amount=5):
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"{ctx.message.author.display_name} has deleted {len(deleted)} messages")

    @commands.command()
    async def roll(self , ctx, *, side):
        if side.isdigit():
            r = random.choice(range(int(side)))
            if r == 0:
                r = int(side)
            await ctx.send(f"Dice roled. Its {r}!")
        if not side.isdigit():
            await ctx.send(f":facepalm: You have to insert a number not ***{side}*** .")
    
    @commands.command()
    async def flip(self , ctx):
        await ctx.send(f"Coin fliped.\n its {random.choice(LUCK_SPIN)} !")

    @commands.command()
    async def ysearch(self , ctx, *, search):
        await ctx.send(get_youtube_data(search))
    

    @commands.command()
    async def choose(self ,ctx, *, words):
        await ctx.send(choose_word(words))

def setup(client):
    client.add_cog(featurescog(client))
