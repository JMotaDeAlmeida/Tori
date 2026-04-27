from discord.ext import commands
import asyncio

class Pomodoro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def pomodoro(self, ctx, *args):
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
        await asyncio.sleep(study*60)
        await ctx.send(f"Foco acabou")
        await asyncio.sleep(breaks*60)
        await ctx.send(f"Descanso acabou")

    @commands.command()
    async def check_voice(self, ctx):
        author = ctx.author.voice
        if author == None:
            await ctx.send("Não esta no voice")
        else:
            await ctx.send(ctx.author.voice.channel)

async def setup(bot):
    await bot.add_cog(Pomodoro(bot))