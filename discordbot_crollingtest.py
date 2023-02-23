import requests
from bs4 import BeautifulSoup

response = requests.get("https://paullab.co.kr/stock.html")

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

#print(soup.select('#update')[0].text)

#print(soup.select('.main')[2])

oneStep = soup.select('.main')[2]

# print(oneStep.select('tbody > tr')) # 테이블만 가져온 후 가장 위에 제목행을 날려야함 

twoStep = oneStep.select('tbody > tr')[1:]

# woStep[0].select('td')[1].text.replace(',', '') # 실제 데이터값만 추출 

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

print(listJson)