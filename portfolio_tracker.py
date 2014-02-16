#!/usr/bin/env python

import string
from prettytable import PrettyTable

#stocks are order for: title, name of the company, purchase price, latest price

stocks = {'Google':["GOOG","Google",100,1134.18,1202.80],\
'Groupon':["GRPN","Groupon",100,10.46,10.51],\
'3D Systems Corporation':["DDD","3D Systems Corporation",50,66.91,73.83],\
'Facebook':["FB","Facebook",50,64.33,67.09]}

portfolio = PrettyTable(['Company','Shares','Purchase','Latest','Value','Gain'])
portfolio.align['Company'] = 'l'
portfolio.padding_width = 1
for x in stocks:
	portfolio.add_row([stocks[x][1]+' ('+stocks[x][0]+')',\
		stocks[x][2],\
		stocks[x][3],\
		stocks[x][4],\
		stocks[x][2]*stocks[x][4],\
		str(round((-stocks[x][3]+stocks[x][4])/stocks[x][3]*100,1))+'%'])
print portfolio
