import requests
from datetime import datetime

CHANNEL_ACCESS_TOKEN = "b3a29bc75994fafd4270a885675c3852"
USER_ID = "2008893027"

def send_line(text):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": text}]
    }
    requests.post(url, headers=headers, json=data)

def main():
    today = datetime.now().strftime("%Y/%m/%d")
    message = f"""🎰 新台速報（{today}）

【パチンコ新台】
・e ゴジラ対エヴァンゲリオン2
・e 範馬刃牙199ver.

【スマスロ新台】
・スマスロ 北斗の拳 転生の章2
・スマスロ 鉄拳6

※正式導入・予定含む
"""
    send_line(message)

if __name__ == "__main__":
    main()
