# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('pung')

@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")

@bot.command()
async def inverse(ctx, message):
    await ctx.send(message[::-1])


bot.run(os.environ["DISCORD_TOKEN"])
