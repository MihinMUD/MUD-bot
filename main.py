import discord
from discord.ext import commands
import random

TOKEN = ""

client = commands.Bot(command_prefix="mud ", help_command=None)


client.load_extension("cogs.featurescog")
client.load_extension("cogs.helpcog")
client.load_extension("cogs.chatcog")

help_embed = discord.Embed(
title="Commands",
description=f"`<something>`= required \n \n`(something)` = optional",
colour=discord.Colour.blue()
)

def help_r(command , descp):
    help_embed.add_field(name=f":white_check_mark:  ```{command}```", value=f"{descp}",inline=True)

help_r("leave" , "Make Me leave the server")
help_r("figlet <words>" , "Figlet give words")
help_r("clr <amount>" , "clr amount of messages")
help_r("flip <sides>" , "Roll a dice of given sides")
help_r("ysearch <term>" , "Search youtube for something")
help_r("choose <words>" , "Choose randomly from given words")
help_r("amazed" , "Use when you amazed")
help_r("hi" , "Search youtube for something")
help_r("laugh" , "Make me laugh")
help_r("wink" , "Wink!")
help_r("hugry" , "I m Hungry!")
help_r("yay" , "Yay")
help_r("say <thing>" , "Make me repeat something")
help_r("annoy <person>" , "Use when there is a annoying person")
help_r("8ball <question>" , "Ask Yes/No question!")
help_r("calc <calculation>" , "Let Me calculate something")

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for prefix mud'))


@client.command()
async def help(ctx):
    await ctx.send(embed =help_embed)


client.run(TOKEN)
