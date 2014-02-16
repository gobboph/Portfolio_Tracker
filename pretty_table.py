#!/usr/bin/env python

from prettytable import PrettyTable

#x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
#x.align["City name"] = "l" # Left align city names
#x.padding_width = 1 # One space between column edges and contents (default)
#x.add_row(["Adelaide",1295, 1158259, 600.5])
#x.add_row(["Brisbane",5905, 1857594, 1146.4])
#x.add_row(["Darwin", 112, 120900, 1714.7])
#x.add_row(["Hobart", 1357, 205556, 619.5])
#x.add_row(["Sydney", 2058, 4336374, 1214.8])
#x.add_row(["Melbourne", 1566, 3806092, 646.9])
#x.add_row(["Perth", 5386, 1554769, 869.4])
#print x

#y = PrettyTable()
#y.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
#y.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
#y.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
#y.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
#print y

#stocks = {'Google':["GOOG","Google",100,1134.18,1202.80],\
#'Groupon':["GRPN","Groupon",100,10.46,10.51],\
#'3D Systems Corporation':["DDD","3D Systems Corporation",50,66.91,73.83],\
#'Facebook':["FB","Facebook",50,64.33,67.09]}

f = open('stocks.txt',r)
for line in f:
	x = f.readline().split(',')
	print x
f.close()

def show_portfolio(dict):
	portfolio = PrettyTable(['Company','Shares','Purchase','Latest','Value','Gain'])
	portfolio.align['Company'] = 'l'
	portfolio.padding_width = 1
	for x in stocks:
		portfolio.add_row([dict[x][1]+' ('+dict[x][0]+')',\
			dict[x][2],\
			dict[x][3],\
			dict[x][4],\
			dict[x][2]*dict[x][4],\
			str(round((-dict[x][3]+dict[x][4])/dict[x][3]*100,1))+'%'])
	print portfolio

#show_portfolio(stocks)