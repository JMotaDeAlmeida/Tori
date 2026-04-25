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

@bot.command()
async def pomodoro(ctx, study:int, breaks:int):
    await ctx.send(f"Iniciando foco de {study} e descanso de {breaks} minutos")

#client = discord.Client(intents=intents)
#
#@client.event
#async def on_ready():
#    print(f"We have logged in as {client.user}")
#
#
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    
#    if message.content.startswith("$hello"):
#        await message.channel.send("Hello!")
#
#client.run(DISCORD_TOKEN)

bot.run(DISCORD_TOKEN)