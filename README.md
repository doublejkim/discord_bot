# discord_bot
Discord Bot Test Sample

# 준비
discord 라이브러리 설치

```shell
pip install discord.py
```

# 디스코드에서의 셋팅
디스코드 봇 사이트에서 Bot Application 생성 후 application id 를 이용해 다음 url 로 접근.
- 디스코드 대화방(서버) 에 추가

```
https://discord.com/oauth2/authorize?client_id=APPLICATION_ID&permissions=8&scope=bot
```
# Token 관련 주의사항
Token을 소스내에 명시하지 않고 `.discordbot_token` 파일에 기술하여 읽어오도록 하였음
