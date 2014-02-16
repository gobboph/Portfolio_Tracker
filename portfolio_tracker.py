#!/usr/bin/env python

import string
from prettytable import PrettyTable


#stocks are order for: title, name of the company, number of shares, purchase price, latest price
stocks = {'Google':["GOOG","Google",100,1134.18,1202.80],\
'Groupon':["GRPN","Groupon",100,10.46,10.51],\
'3D Systems Corporation':["DDD","3D Systems Corporation",50,66.91,73.83],\
'Facebook':["FB","Facebook",50,64.33,67.09]}




# !!!DEFINING RELEVANT FUNCTIONS!!!

def show_portfolio(dict):
#This works only for dictionary defined in such a way that for each key there is an array structured like this:
#title, name of the company, number of shares, purchase price, latest price
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

def add_stock(dict):
#Function to add a stock to portfolio, work with the same dictionary structure as above
	new_stock = str(raw_input('Write the name of the company you want to add \n'))
	new_symbol = str(raw_input('And its new_symbol, please \n'))
	num_share = int(raw_input('how many of those do you have? \n'))
	purch_price = round(float(raw_input('And how much did you pay for them? \n')),1)
	x = raw_input('Is the price now the same as the when you bought it? (Y/N) ').upper()
	if x=='Y':
		latest_price = purch_price
	elif x=='N':
		latest_price = round(float(raw_input('Then what is its price now?\n')),1)
	else:
		print 'you should have been more precise in pressing y or n, now I am shutting down'
		exit()
	dict[new_stock]=[]
	dict[new_stock].append(new_symbol)
	dict[new_stock].append(new_stock)
	dict[new_stock].append(num_share)
	dict[new_stock].append(purch_price)
	dict[new_stock].append(latest_price)

def del_stock(dict):
#Function to delete stock from portfolio
	del_stock = raw_input('Which company have you sold? (capitalize correctly, you have the table right in front of you) ')
	if del_stock not in stocks:
		print 'You did not have that, moron, so I am shutting down now'
	else:
		del stocks[del_stock]


# !!!MAIN!!!

def main():
	print 'This is your portfolio now'
	show_portfolio(stocks)
	UpDate = raw_input('If you want to update it press U, otherwise you can (E)xit. ').upper()
	if UpDate == 'U':
		AddDel = raw_input('Do you want to (A)dd or (D)elete any stock? ').upper()
		if AddDel == 'A':
			add_stock(stocks)
		elif AddDel == 'D':
			del_stock(stocks)
		else:
			print 'I did not undertsand, therefore exiting the program. Be more careful with typing, asshole.'
			exit()
	elif UpDate == 'E':
		exit()

while True:
	main()

