#!/usr/bin/env python

import string
from prettytable import PrettyTable


#stocks are order for: title, name of the company, number of shares, purchase price, latest price
#stocks = {'Google':["GOOG","Google",100,1134.18,1202.80],\
#'Groupon':["GRPN","Groupon",100,10.46,10.51],\
#'3D Systems Corporation':["DDD","3D Systems Corporation",50,66.91,73.83],\
#'Facebook':["FB","Facebook",50,64.33,67.09]}




# !!!DEFINING RELEVANT FUNCTIONS!!!

def dict_from_file(file):
#This function reads from a file and writes a dictionary from it.
#The file needs to have on each line the structure: title, name of the company, number of shares, purchase price, latest price
#ONLY SEPARATED BY A COMMA
	dictionary = {}
	f = open(file,'r')
	for line in f:
		x = line.strip('\n').split(',')
		dictionary[x[1]] = []
		dictionary[x[1]].append(x[0])
		dictionary[x[1]].append(x[1])
		dictionary[x[1]].append(round(float(x[2]),2))
		dictionary[x[1]].append(round(float(x[3]),2))
		dictionary[x[1]].append(round(float(x[4]),2))
		#print stocks[x[1]]
	f.close()
	return dictionary


def show_portfolio(dict):
#This works only for dictionary defined in such a way that for each key there is an array structured like this:
#title, name of the company, number of shares, purchase price, latest price
	portfolio = PrettyTable(['Company','Shares','Purchase','Latest','Value','Gain'])
	portfolio.align['Company'] = 'l'
	portfolio.padding_width = 1
	tot_latest = 0
	for x in dict:
		portfolio.add_row([dict[x][1]+' ('+dict[x][0]+')',\
			dict[x][2],\
			dict[x][3],\
			dict[x][4],\
			dict[x][2]*dict[x][4],\
			str(round((-dict[x][3]+dict[x][4])/dict[x][3]*100,1))+'%'])
		tot_latest += dict[x][2]*dict[x][4]
	portfolio.add_row(['','','','','',''])
	portfolio.add_row(['TOT','','','',tot_latest,'tot_gain'])
	print portfolio

def write_new_line(file):
#This function writes a new line in the file with the info for the portfolio. It will substitute add_stock
	new_stock = str(raw_input('Write the name of the company you want to add \n'))
	new_symbol = str(raw_input('And its new_symbol, please \n'))
	num_share = raw_input('how many of those do you have? \n')
	purch_price = raw_input('And how much did you pay for them? \n')
	x = raw_input('Is the price now the same as the when you bought it? (Y/N) ').upper()
	if x=='Y':
		latest_price = purch_price
	elif x=='N':
		latest_price = raw_input('Then what is its price now?\n')
	else:
		print 'you should have been more precise in pressing y or n, now I am shutting down'
		exit()
	f = open(file,'a')
	f.write(new_symbol+','+new_stock+','+num_share+','+purch_price+','+latest_price+'\n')

def write_port_to_file(dict,file):
	f = open(file,'w')
	for key in dict:
		f.write(dict[key][1]+','+dict[key][0]+','+dict[key][2]+','+dict[key][3]+','+dict[key][4])
	f.close()


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
	if del_stock not in dict:
		print 'You did not have that, moron, so I am shutting down now'
		exit()
	else:
		del dict[del_stock]


# !!!MAIN!!!

def main():
	stocks = dict_from_file('stocks.txt')
	print 'This is your portfolio now'
	show_portfolio(stocks)
	UpDate = raw_input('If you want to update it press U, otherwise you can (E)xit. ').upper()
	if UpDate == 'U':
		AddDel = raw_input('Do you want to (A)dd or (D)elete any stock? ').upper()
		if AddDel == 'A':
			write_new_line('stocks.txt')
		elif AddDel == 'D':
			del_stock(stocks)
		else:
			print 'I did not undertsand, therefore exiting the program. Be more careful with typing, asshole.'
			exit()
	elif UpDate == 'E':
		exit()

while True:
	main()

