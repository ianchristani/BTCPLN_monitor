from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
from urllib.request import urlopen

#scraping the data in the source
def getquote():

    #souces adresses
    src = {'Oil': 'https://www.marketwatch.com/investing/future/crude%20oil%20-%20electronic',
    'ETHUSD': 'https://www.marketwatch.com/investing/cryptocurrency/ethusd',
    'BTCPLN': 'https://www.marketwatch.com/investing/cryptocurrency/btcpln'
    }

    #variable to build the interface
    row = 1
    
    for n in src:
        pg =  urlopen(src[n])
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