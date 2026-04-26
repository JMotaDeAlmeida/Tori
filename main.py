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

@bot.command()
async def pomodoro(ctx, *args):
    if len(args) != 2:
        await ctx.send("Assim não funciona. Tenta colocar o periodo de estudo e descanso")
        return

    try:
        study = int(args[0])
        breaks = int(args[1])
    except ValueError:
        await ctx.send("Insira números válidos")
        return

    if study <= 0 or breaks <= 0:
        await ctx.send("Valores precisam ser positivos")
        return

    await ctx.send(f"Iniciando foco de {study} minutos e descanso de {breaks} minutos")

bot.run(DISCORD_TOKEN)