import discord
import random
from discord.ext import commands

BALL = [
    "It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy try again",
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don’t count on it",
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no",
]
GREATINGS=[
    "Hi :)",
    "Hello!",
    "hi, Nice to meet you!",
]

class chatcog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(pass_context=True)
    async def amazed(self ,ctx):
        await ctx.send(f"{ctx.message.author} is Amazed!")
        await ctx.send("https://tenor.com/view/amazed-cat-gif-5025844")


    @commands.command(aliases=["hello"])
    async def hi(self ,ctx):
        await ctx.send(random.choice(GREATINGS))


    @commands.command(aliases=["thx", "ty", 'thankyou'])
    async def thanks(self , ctx):
        thanks = [
            "Your Welcome!",
            "No problem :)"
        ]
        await ctx.send(random.choice(thanks))


    @commands.command()
    async def crazy(self , ctx, *, person):
        await ctx.send(f"{person} is crazy.. ")
        await ctx.send("https://media.giphy.com/media/eaECZB7V6GACc/giphy.gif")


    @commands.command()
    async def laugh(self , ctx):
        await ctx.send("https://tenor.com/view/despicable-me-minions-laugh-laughing-lol-gif-3571116")


    @commands.command()
    async def wink(self , ctx):
        await ctx.send("https://tenor.com/view/mr-bean-wink-trust-me-%E0%A4%86%E0%A4%81%E0%A4%96-gif-10540459")


    @commands.command()
    async def hungry(self ,ctx):
        await ctx.send(
            "https://tenor.com/view/its-time-to-eat-garfield-knife-and-fork-eating-time-dinner-time-gif-19321135")


    @commands.command()
    async def yay(self , ctx):
        await ctx.send("Yay!")


    @commands.command()
    async def say(self , ctx, *, thing):
        await ctx.send(thing)


    @commands.command()
    async def annoy(self , ctx, *, person):
        await ctx.send(f"{person} is very annoying")
        await ctx.send("https://tenor.com/view/nope-monkey-laptop-angry-furious-gif-7316263")


    @commands.command(aliases=["8ball"])
    async def _8ball(self , ctx, *, question):
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(BALL)}")


    @commands.command(aliases=["calc"])
    async def c(self ,ctx, *, sum):
        await ctx.send(eval(sum))



def setup(client):
    client.add_cog(chatcog(client))