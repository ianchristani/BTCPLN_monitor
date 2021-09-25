from bs4 import BeautifulSoup
from urllib.request import urlopen

ls = []

#getting the data in the source
def getquote():   
    pg =  urlopen('https://www.marketwatch.com/investing/cryptocurrency/btcpln')
    soup = BeautifulSoup (pg,'html.parser')
    quote = soup.find_all('bg-quote')
    btc_quote = str((quote[45].contents[0]))

    #treating the string
    btc_quote = btc_quote.replace(',','.')
    btc_quote = float(btc_quote)

getquote()