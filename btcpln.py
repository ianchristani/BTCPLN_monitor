'''
This script was the first idea, first scratching. The MONITOR file is more complete, developed and work in a stand alone mode.
I will keep this file just as a register, but the project will be developed from MONITOR.PY.
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

hdt = {}

#getting the data in the source
def getquote(hdt):
    quote_p = ''
    while True:    
        pg =  urlopen('https://www.marketwatch.com/investing/cryptocurrency/btcpln')
        soup = BeautifulSoup (pg,'html.parser')
        quote = soup.find_all('bg-quote')
        btc_quote = str((quote[45].contents[0]))

        #building the storic data
        if btc_quote != quote_p:
            quote_p = btc_quote

            #treating the string
            btc_quote = btc_quote.replace(',','.')
            btc_quote = float(btc_quote)

            #adding the time to the quote
            quote_time = str(time.strftime('%H:%M:%S'))
            hdt [quote_time] = btc_quote
            hdt = dict(sorted(hdt.items(), key=lambda item:item[1]))

            print(hdt)

getquote(hdt)