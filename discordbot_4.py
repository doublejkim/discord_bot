import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import datetime

app = commands.Bot(command_prefix='/', intents=discord.Intents.all())
today = datetime.datetime.today()

@app.event
async def on_ready():
    print(f'{app.user.name} 연결 성공')
    print(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command(aliases=['따라하기', 'f'])
async def 정보(ctx):

    try:
        response = requests.get("https://www.jejuiucc.or.kr/default/Bd/list.php?btable=notice")

        response.encoding = 'utf-8'
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        totalInfo = soup.select('tr')

        for info in totalInfo[1:6]:
            dataNo, dataTitle, dataWritor, dataFile, dataCreateDate, dataCnt = info.select('td')
            await ctx.send(f'```기관 : 제주산학융합원\n제목 : {dataTitle.text}\n날짜 : {dataCreateDate.text}\n```링크 :  https://www.jejuiucc.or.kr/default/Bd/{dataTitle.a["href"]}\n\n')
            await ctx.send(f'---')
    except:
        await ctx.send(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분 정보로직 오류 발생')

f = open(".discordbot_token", 'r')
token = f.readline()
f.close()

app.run(token)
