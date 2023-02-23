import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

app = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@app.event
async def on_ready():
    print(f'{app.user.name} 연결 성공')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command(aliases=['따라하기', 'f'])
async def 주가(ctx, arg):

    response = requests.get("https://paullab.co.kr/stock.html")

    response.encoding = 'utf-8'
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    mainInfo = soup.select('.main')[1]
    marketCap = mainInfo.select('td')[0].text  # 시가 총액 
    marketCapRank = mainInfo.select('td')[1].text  # 시가총액 순위
    

    oneStep = soup.select('.main')[2]
    twoStep = oneStep.select('tbody > tr')[1:]

    ## 실제 데이터값만 추출 

    listDate = []           # 날짜
    listLastValue = []      # 종가
    listDiffPercentage = [] # 전일비
    listDealVolume = []     # 거래량

    for i in twoStep:
        listDate.append(i.select('td')[0].text)
        listLastValue.append(i.select('td')[1].text.replace(',', ''))
        listDiffPercentage.append(i.select('td')[2].text.replace(',', '').replace('\n', '').strip())
        listDealVolume.append(i.select('td')[6].text.replace(',', ''))

    # to json..
    listJson = []

    for i in range(len(listDate)):
        listJson.append({
            '날짜':listDate[i],
            '종가':listLastValue[i],
            '전일비':listDiffPercentage[i],
            '거래량':listDealVolume[i]
        })

    if arg == '시가총액':
        await ctx.send(marketCap)
    elif arg == '시가총액순위':
        await ctx.send(marketCapRank)
    elif arg == '전일종가':
        await ctx.send(listJson[0]['종가'])
    elif arg == '최근한달거래':
        for i in listJson:
            await ctx.send(f'```날짜 : {str(i["날짜"])}\n종가 : {str(i["종가"])}\n전일비 : {str(i["전일비"])}\n거래량 : {str(i["거래량"])}```')

f = open(".discordbot_token", 'r')
token = f.readline()
f.close()

app.run(token)
