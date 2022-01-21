from bs4 import BeautifulSoup
import requests
import time, datetime
import telepot

TOKEN = '5072386393:AAG2wOS-zTxIrPzE16y0pZvvY31GXq3LUDo'
telegram_id = '5042631031'
bot = telepot.Bot(TOKEN)

def dart_checking():
    time.sleep(1)
    while True:
        today_time = datetime.datetime.today()
        hhmm = str(today_time)[11:16]

        if hhmm == "15:30":
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

            msg = report_company.text.strip(), report_title.get('title').split()[0], report_submit.get('title'), "https://dart.fss.or.kr" + report_title.get('href')

            bot.sendMessage(telegram_id, str(msg))

def time_check():

    time.sleep(1)

    while True:
        today_time = datetime.datetime.today()
        tt = str(today_time)
        hhmmss, hh = tt[11:19], int(tt[11:13])
        print(hhmmss)

        if tt[0] == "0":
            hh = int(tt[12])

        if hhmmss == "08:30:00" or 8 < hh < 10:
            dart_checking()
            break

        time.sleep(1)

time_check()