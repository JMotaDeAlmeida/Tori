import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def main():
    async with bot:
        await bot.load_extension("commands.pomodoro")
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())