#!/usr/bin/env python

import string
from prettytable import PrettyTable

#stocks are order for: title, name of the company, number of shares, purchase price, latest price

stocks = {'Google':["GOOG","Google",100,1134.18,1202.80],\
'Groupon':["GRPN","Groupon",100,10.46,10.51],\
'3D Systems Corporation':["DDD","3D Systems Corporation",50,66.91,73.83],\
'Facebook':["FB","Facebook",50,64.33,67.09]}


#desiging portfolio table

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

print 'This is your portfolio at the moment'
print portfolio

UpDate = raw_input('If you want to update it press U, otherwise admire how nice it is.').upper()

if UpDate == 'U':
	AddDel = raw_input('Do you want to (A)dd or (D)elete any stock?').upper()
	if AddDel == 'A':
		new_stock = str(raw_input('Write the name of the company you want to add \n'))
		new_symbol = str(raw_input('And its new_symbol, please \n'))
		num_share = raw_input('how many of those do you have? \n')
		purch_price = raw_input('And how much did you pay for them? \n')
		x='a'
		count=1
		while x!='Y' or x!='N'or count!=10:
			x = raw_input('Is the price now the same as the when you bought it? (Y/N)').upper()
			count+=1
			if count==10:
				print 'Well, too many times to try and press Y or N, idiot, I am shutting down'
		if x=='Y':
			latest_price = purch_price
		elif x=='N':
			latest_price = raw_input('Then what is its price now?\n')
		stocks[new_stock]=[]
		stocks[new_stock].add(new_symbol)
		stock[new_stock].add(new_stock)
		stock[new_stock].add(num_share)
		stock[new_stock].add(purch_price)
		stock[new_stock].add(latest_price)

	elif AddDel == 'D':
		del_stock = raw_input('Which company have you sold? (capitalize correctly, you have the table right in fron of you)')
		if del_stock not in stocks:
			print 'You did not have that, moron, so I am shutting down now'
		else:
			del stocks[del_stock]

	else:
		print 'I did not undertsand, therefore exiting the program. Be more careful with typing, asshole.'
		exit()

print 'I am printing the updated table for you now, then shutting down. (No you can not update more than once at the moment)'

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


exit()

