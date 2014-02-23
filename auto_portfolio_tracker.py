#!/usr/bin/env python

import string
from prettytable import PrettyTable
import ystockquote


# !!!DEFINING RELEVANT FUNCTIONS!!!

def dict_from_file(file):
#This function reads from a file and writes a dictionary from it.
#The file needs to have on each line the structure: name of the company, title, number of shares, purchase price, latest price
#ONLY SEPARATED BY A COMMA
	dictionary = {}
	f = open(file,'r')
	for line in f:
		x = line.strip('\n').split(',')
		dictionary[x[0]] = []
		dictionary[x[0]].append(x[0])
		dictionary[x[0]].append(x[1])
		dictionary[x[0]].append(round(float(x[2]),1))
		dictionary[x[0]].append(round(float(x[3]),2))
		dictionary[x[0]].append(round(float(x[4]),2))
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
	tot_purchase = 0
	for x in dict:
		portfolio.add_row([dict[x][0]+' ('+dict[x][1]+')',\
			dict[x][2],\
			dict[x][3],\
			dict[x][4],\
			dict[x][2]*dict[x][4],\
			str(round((-dict[x][3]+dict[x][4])/dict[x][3]*100,2))+'%'])
		tot_latest += dict[x][2]*dict[x][4]
		tot_purchase += dict[x][2]*dict[x][3]
	portfolio.add_row(['','','','','',''])
	if tot_purchase==0:
		portfolio.add_row(['TOT','',tot_purchase,'',tot_latest,'-'])
	else:
		portfolio.add_row(['TOT','','','',tot_latest,str(round((tot_latest-tot_purchase)/tot_purchase*100,2))+'%'])
	print portfolio

def write_dict_to_file(dict,file):
#This writes the dictionary to file the way I would like to.
	f = open(file,'w')
	for key in dict:
		f.write(dict[key][0]+','+dict[key][1]+','+str(dict[key][2])+','+str(dict[key][3])+','+str(dict[key][4])+'\n')
	f.close()


def add_stock(dict):
#Function to add a stock to portfolio, work with the same dictionary structure as above
	new_stock = str(raw_input('Company Name: '))
	new_symbol = str(raw_input('Symbol: '))
	num_share = raw_input('Number of stocks purchased: ')
	purch_price = ystockquote.get_bid_realtime(new_symbol) #raw_input('Purchase Price: ')
	latest_price = purch_price #raw_input('Latest Price: ')
	dict[new_stock]=[]
	dict[new_stock].append(new_stock)
	dict[new_stock].append(new_symbol)
	dict[new_stock].append(num_share)
	dict[new_stock].append(purch_price)
	dict[new_stock].append(latest_price)

def del_stock(dict):
#Function to delete stock from portfolio
	while True:
		del_stock = raw_input('Which company have you sold? ')
		if del_stock not in dict:
			print 'Can you repeat? (company name, capitalize correctly) '
			#exit()
		else:
			del dict[del_stock]
			break

def update_price(dict):
	while True:
		up_stock = raw_input('Company to update: ')
		if up_stock not in dict:
			print 'Can you repeat? (company name, capitalize correctly) '
		else:
			print 'Updating...'
			dict[up_stock][4] = ystockquote.get_bid_realtime(dict[up_stock][1]) #round(float(raw_input('New price: ')),2)
			break

def create_file():
	print 'Creating a new text file...'
	name = raw_input('name of file: ')+'.txt'
	open(name,'w')
	name.close()


# !!!MAIN!!!

def main():
	choice = raw_input('(W)rite a new file or (U)pload an existing one: ').upper()
	if choice == U:
		upload = raw_input('Which file do you want to upload? ')
	else:
		create_file()
	#upload = raw_input('Which file do you want to upload? ')
	while True:
		stocks = dict_from_file(upload)
		print ''
		print 'This is your portfolio now'
		print ''
		show_portfolio(stocks)
		UpDate = raw_input('(A)dd/(D)elete stock, update a (P)rice, (U)pload another file, (Q)uit. ').upper()
		if UpDate == 'A':
			add_stock(stocks)
			write_dict_to_file(stocks,upload)
		elif UpDate == 'D':
			del_stock(stocks)
			write_dict_to_file(stocks,upload)
		elif UpDate == 'P':
			update_price(stocks)
			write_dict_to_file(stocks,upload)
		elif UpDate == 'U':
			break
		elif UpDate == 'Q':
			exit()
		else:
			print ''
			print 'Sorry, I did not understand what you want to do, here are your options again.'
		#write_dict_to_file(stocks,upload)

#upload = raw_input('Which file do you want to upload? ')
while True:
	main()


#Functions I do not seem to use at the moment

def write_new_line(file):
#This function writes a new line in the file with the info for the portfolio. It will substitute add_stock
	new_stock = str(raw_input('Company Name: '))
	new_symbol = str(raw_input('Symbol: '))
	num_share = raw_input('Number of stocks purchased: ')
	purch_price = raw_input('Purchase Price: ')
	latest_price = raw_input('Latest Price: ')
	f = open(file,'a')
	f.write(new_stock+','+new_symbol+','+num_share+','+purch_price+','+latest_price+'\n')
	f.close()

