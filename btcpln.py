from bs4 import BeautifulSoup
from urllib.request import urlopen

ls = []

#getting the data in the source
def getquote():
    tmp =[]    
    pg =  urlopen('https://www.marketwatch.com/investing/cryptocurrency/btcpln')
    soup = BeautifulSoup (pg,'html.parser')
    quote = soup.find_all('bg-quote')
    btc_quote = str((quote[45].contents[0]))

    print(btc_quote)
    btc_qutoe = btc_quote.replace (',','.')
    print(btc_quote)


getquote()