import yfinance as yf
import pywhatkit
import datetime
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.google.com/finance/quote/SENSEX:INDEXBOM'
html_text = requests.get(base_url).text
soup = BeautifulSoup(html_text, 'html.parser')
div = soup.find("div", {"class": "YMlKec fxKbKc"}) ##Web scrapping
sensex = float(div.text.replace(',', ''))

while True:
    msft = yf.Ticker("^BSESN")
    print(msft.info)
    start = msft.info["regularMarketOpen"] ##Market open price

    today =datetime.datetime.now()
    if today.hour>9 and today.hour<16: ## 9AM - 4PM this script will run
        print("Script run time -", today)
        pywhatkit.sendwhatmsg("+91**********", "Sensex current value: {}".format(sensex),  today.hour, today.minute+1)

        today =datetime.datetime.now()
        if sensex>53000:
            pywhatkit.sendwhatmsg("+91**********", "Sensex is above 53000",  today.hour, today.minute+1)

        if sensex<50000:
            pywhatkit.sendwhatmsg("+91**********", "Sensex is below 50000",today.hour, today.minute+1)
            
        today =datetime.datetime.now()
        if (sensex-start)>2000:
            pywhatkit.sendwhatmsg("+91**********", "Sensex is crazyly moving up",today.hour, today.minute+1)
        elif (sensex-start)>1000:
            pywhatkit.sendwhatmsg("+91**********", "Sensex is up by 1000 pts",today.hour, today.minute+1)

        if (start-sensex)>2000:
            pywhatkit.sendwhatmsg("+91**********", "Sensex is crazyly moving down",today.hour, today.minute+1)
        elif (start-sensex)>1000:
            pywhatkit.sendwhatmsg("+91**********", "Sensex is down by 1000 pts",today.hour, today.minute+1)
        
    

    time.sleep(3600)
    
