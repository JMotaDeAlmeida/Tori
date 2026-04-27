import asyncio
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


bot.run(DISCORD_TOKEN)