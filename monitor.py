from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
from urllib.request import urlopen

#scraping the data in the source
def getquote():

    #souces adresses
    src1 = {'Oil': 'https://www.marketwatch.com/investing/future/crude%20oil%20-%20electronic',
    'ETHUSD': 'https://www.marketwatch.com/investing/cryptocurrency/ethusd',
    'BTCPLN': 'https://www.marketwatch.com/investing/cryptocurrency/btcpln'
    }

    #the ones whom use the new filter method
    src2 = {
    'Gold': 'https://www.marketwatch.com/investing/future/gold',
    'EURUSD': 'https://www.marketwatch.com/investing/currency/eurusd',
    'PLNUSD': 'https://www.marketwatch.com/investing/currency/plnusd?mod=over_search',
    'Dow Jones': 'https://www.marketwatch.com/investing/future/djia%20futures',
    'SP500 fut': 'https://www.marketwatch.com/investing/future/sp%20500%20futures',
    }

    #variable to build the interface
    row = 1
    
    for n in src1:
        pg =  urlopen(src1[n])
        soup = BeautifulSoup (pg,'html.parser')
        quote = soup.find_all('bg-quote')
        mkt_time = str((quote[44].contents[0]))
        mkt_quote = str((quote[45].contents[0]))
        mkt_perc = str((quote[48].contents[0]))
        info = f'     {mkt_quote}          {mkt_perc}           {mkt_time}'

        #the GUI dinamic part
        ttk.Label(mainframe, text= n).grid(row=row,column=0, sticky=(W, E))
        ttk.Label(mainframe, text= info).grid(row=row,column=1, sticky=(W, E))
        row += 1

    for n in src2:
        pg =  urlopen(src2[n])
        soup = BeautifulSoup (pg,'html.parser')
        quote = soup.find_all('bg-quote')
        #using other way to filter to get the data
        quote1 = soup.find_all('span', class_ = 'value')
        mkt_time = str((quote[44].contents[0]))
        #using the new filter
        mkt_quote = str((quote1[6].contents[0]))
        #still using the old one, but now this data is inside a span
        mkt_perc = str(soup.select_one("span[class*=change--percent--q]").text)
        info = f'     {mkt_quote}          {mkt_perc}           {mkt_time}'

        #the GUI dinamic part
        ttk.Label(mainframe, text= n).grid(row=row,column=0, sticky=(W, E))
        ttk.Label(mainframe, text= info).grid(row=row,column=1, sticky=(W, E))
        row += 1

        #keeping updating every 10s
        monitor.after(10000,getquote)

#the GUI
monitor = Tk()
monitor.title("market monitor")

mainframe = ttk.Frame(monitor, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
monitor.columnconfigure(0, weight=1)
monitor.rowconfigure(0, weight=1)

getquote()

monitor.mainloop()