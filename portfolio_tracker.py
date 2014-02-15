#!/usr/bin/env python

import string
from prettytable import PrettyTable

#stocks are order for: title, name of the company, purchase price, latest price

stocks = [["GOOG","Google",100,1134.18,1202.80],["GRPN","Groupon",100,10.46,10.51],["DDD","3D Systems Corporation",50,66.91,73.83],["FB","Facebook",50,64.33,67.09]]

portfolio = PrettyTable(['Company','Shares','Purchase','Latest','Value','Gain'])
portfolio.align['Company'] = 'l'
portfolio.padding_width = 1
for i in range(len(stocks)):
	portfolio.add_row([stocks[i][1]+' ('+stocks[i][0]+')', stocks[i][2],stocks[i][3],stocks[i][4],stocks[i][2]*stocks[i][4],str(round((-stocks[i][3]+stocks[i][4])/stocks[i][3]*100,1))+'%'])
print portfolio
