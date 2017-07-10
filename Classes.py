# This code is has been written in order to assist Fabian Ng with the update of His excel file #

import pandas as pd 
import os
from pandas import ExcelWriter
from pandas import ExcelFile


class Trade:
	def __init__(self, p1, p2, p3, p4, p10):
		self.oDate=p1
		self.currency=p2
		self.BS=p3 
		self.oPrice=p4
		self.fB=p10
		self.cDate=None
		self.cPrice=None
		self.pips=None
		self.pipsD=None 
#		os.chdir("/Users/mezzatab/FN4X/REPORTS")
		file = '/Users/mezzatab/FN4X/ShareHolders/ShareHolders.xlsx'
		xl=pd.read_excel(file, sheetname='Sheet1')
		self.nameList = xl["Share Holders"]
		self.budgetList=xl["Share Money"]
		self.shareList = xl["Share Dist"]

		file = '/Users/mezzatab/FN4X/ShareHolders/OpenTrades.xlsx'
		xd=pd.read_excel(file, sheetname='Sheet1')



	def final(self, p5, p6, p7, p8):	
		self.cDate=p5
		self.cPrice=p6
		self.pips=p7
		self.pipsD=p8 
		L=len(self.shareList)
		shareMoney=[0]*L
		file = '/Users/mezzatab/FN4X/ShareHolders/ShareHolders.xlsx'
		xl=pd.read_excel(file, sheetname='Sheet1')


		totBal=0
		for i in range(L):
			shareMoney[i]=self.shareList[i]*self.pipsD	
			xl["Share Money"][i]=xl["Share Money"][i]+shareMoney[i]
			totBal+=xl["Share Money"][i]

		for i in range(L):
			x=format(1.0*xl["Share Money"][i]/totBal,'.4f')
			xl["Share Dist"][i]=x
			print(xl["Share Dist"][i],xl["Share Money"][i],totBal)

		writer = ExcelWriter('/Users/mezzatab/FN4X/ShareHolders/Second.xlsx')
		xl.to_excel(writer,'Sheet1')
		writer.save()
	



a=Trade("08-1","USP","S","10",1000)
a.final("09-1","12",120,1200) 	
