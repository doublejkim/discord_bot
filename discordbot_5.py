import discord
from discord.ext import commands
import datetime
from discord import Colour
import asyncio
from discord.ext import tasks

app = commands.Bot(command_prefix='/', intents=discord.Intents.all())
today = datetime.datetime.today()

@app.event
async def on_ready():
    print(f'{app.user.name} 연결 성공')
    print(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분')
    print(f'{app.guilds}')
    g = app.guilds[0]


    # print(g.roles)
    for role in g.roles:
        print(f'id : {role.id}, name : {role.name}')

    # guild = app.get_guild("Guild id")
    # role = gruild.get_role("Role id")
    
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def change_color(ctx):

    g = app.guilds[0]
    r = g.roles[1]
    
    # while True:
        # await r.edit(colour = discord.Colour.blue())
        # await r.edit(colour = discord.Colour.random())
        # await asyncio.sleep(1)

    if neonsign_nickname.is_running():
        neonsign_nickname.stop()
    else:
        neonsign_nickname.start(r)

@tasks.loop(seconds=1)
async def neonsign_nickname(role):

    await role.edit(colour=Colour.random())


f = open(".discordbot_token", 'r')
token = f.readline()
f.close()

app.run(token)
