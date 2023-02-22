import discord
from discord.ext import commands

app = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@app.event
async def on_ready():
    print(f'{app.user.name} 연결 성공')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command(aliases=['따라하기', 'f'])
async def 투표(ctx, *args):

    # print(dir(ctx))
    # print(type(ctx))

    # print(dir(args))
    # print(type(args))

    await ctx.send('투표 시작!!')

    for i in args:
        code_block = await ctx.send(f'```{arg}```')
        await code_block.add_reaction("👍")


f = open(".discordbot_token", 'r')
token = f.readline()
f.close()

app.run(token)
