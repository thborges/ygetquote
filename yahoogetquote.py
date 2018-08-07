import io
import cookielib, urllib2
import datetime
import time
import csv

def get_quote(ticket):
    cj = cookielib.MozillaCookieJar()
    # cj.load signature: filename=None, ignore_discard=False, ignore_expires=False
    cj.load('/Users/thborges/ycookies.txt') 

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    #https://query1.finance.yahoo.com/v7/finance/download/USIM5.SA?period1=1530971942&period2=1533650342&interval=1d&events=history&crumb=x10F8d5X3VX
    ydate = int(time.time())
    yurl = 'https://query1.finance.yahoo.com/v7/finance/download/{0}.SA?period1={1}&period2={1}&interval=1d&events=history&crumb=x10F8d5X3VX'
    furl = yurl.format(ticket, ydate)
    
    req = urllib2.Request(url=furl)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1')

    f = urllib2.urlopen(req)

    quote = '0.0'
    data = f.read().decode('utf-8')
    csvreader = csv.DictReader(io.StringIO(data), delimiter=',')
    for row in csvreader:
        quote = row['Close']
    return quote

#print(get_quote("ITSA4"))

