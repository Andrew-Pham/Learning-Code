import urllib
import urllib2
import json

#url = "http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"
url = "http://query.yahooapis.com/v1/public/yql?"

query = {"q":'select * from yahoo.finance.quote where symbol in ("YHOO","AAPL","GOOG","MSFT")', "env":"http://datatables.org/alltables.env", "format":"json"}

query = urllib.urlencode(query)

#print url+query

result = urllib2.urlopen (url + query)
stock_info = result.read()
#print stock_info 

#f = open("C:\Users\Andrew\Documents\Learning Code\stock info.txt", "w")

#f.write (stock_info)

#f.close()

price = json.loads (stock_info)
googprice = price["query"]["results"]["quote"][2]["DaysHigh"]

print googprice