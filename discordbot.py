import discord
from discord.ext import commands

app = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@app.event
async def on_ready():
    print(f'{app.user.name} 연결 성공')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def hello(ctx):
    await ctx.send('Hello..World..')

@app.command(aliases=['따라하기', 'f'])
async def follow(ctx, *args):
    for i in args:
        await ctx.send(f'```hello {i} world..```')

#@app.event
#async def on_message(msg):
#    await msg.add_reaction("^^")  # imogi...

# token..
# .discordbot_token 파일에 토큰 입력 필요. 
f = open(".discordbot_token", 'r')
token = f.readline()
f.close()

app.run(token)
