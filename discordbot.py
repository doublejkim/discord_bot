import discord
from discord.ext import commands

app = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@app.event
async def on_ready():
    print('f{app.user.name} 연결 성공')