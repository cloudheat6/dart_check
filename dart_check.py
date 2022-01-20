from sqlite3 import Timestamp
from bs4 import BeautifulSoup
import requests
import time, datetime
import telepot

TOKEN = '5072386393:AAG2wOS-zTxIrPzE16y0pZvvY31GXq3LUDo'
telegram_id = '5042631031'
bot = telepot.Bot(TOKEN)

def dart_checking():
    while True:
        today_time = datetime.datetime.today()
        hhmmss = str(today_time)[11:19]

        if hhmmss == "15:30:00":
            time_check()
            break

        r = requests.get("https://dart.fss.or.kr/dsac001/mainAll.do")

        res = BeautifulSoup(r.text, 'html.parser')

        span_num1 = res.find('span', {'class': 'txtCB'})

        total_num1 = int(span_num1.text)

        time.sleep(10)

        r = requests.get("https://dart.fss.or.kr/dsac001/mainAll.do")

        res = BeautifulSoup(r.text, 'html.parser')

        span_num2 = res.find('span', {'class': 'txtCB'})

        total_num2 = int(span_num2.text)

        if total_num2 > total_num1:
            report_company = res.select_one('tbody > tr > td > span > a')
            report_title = res.select_one('tbody > tr > td > a')
            report_submit = res.find('td', {'class' : 'tL ellipsis'})

            msg = str(report_company.text.strip(), report_title['title'].split()[0], report_submit['title'], "https://dart.fss.or.kr" + report_title['href'])

            bot.sendMessage(telegram_id, msg)
            print('메시지 전송 완료')

def time_check():
    while True:
        today_time = datetime.datetime.today()
        hhmmss = str(today_time)[11:19]
        time.sleep(1)

        if hhmmss == "08:30:00":
            dart_checking()
            break

time_check()