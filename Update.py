import pandas as pd 
import os
from pandas import ExcelWriter
from pandas import ExcelFile


class Update:
#	def __init__(self):
#		file = '/Users/mezzatab/FN4X/ShareHolders/ShareHolders.xlsx'
#		xl=pd.read_excel(file, sheetname='Sheet1')
#		self.nameList = xl["Share Holders"]
#		self.shareList = xl["Share Dist"]

	def AddPerson(self, Name, Budget):
		file = '/Users/mezzatab/FN4X/ShareHolders/ShareHolders.xlsx'
		xl=pd.read_excel(file, sheetname='Sheet1', index=False)
		L=len(xl["Share Holders"])
		xl.head()

		xl.loc[L,"Share Holders"]=Name
#		xl["Share Holders"][L]=Name

#		xl["Share Money"][L]=Budget
		xl.loc[L,"Share Money"]=Budget


#		xl["Share Dist"][L]=0
		xl.loc[L,"Share Dist"]=0



		self.nameList = xl.loc[:,"Share Holders"]
		self.shareList = xl.loc[:,"Share Dist"]
		self.shareMoney = xl.loc[:,"Share Money"]
		totBal=0
		for i in range(L+1):
			totBal=totBal+self.shareMoney[i]
		for i in range(L+1):
			self.shareList[i]=1.0*self.shareMoney[i]/totBal

		xl.loc[:,"Share Holders"]=self.nameList
		xl.loc[:,"Share Money"]=self.shareMoney	
		xl.loc[:,"Share Dist"]=self.shareList 


#		print(xl["Share Dist"])
#		print(self.shareList)	
		writer = ExcelWriter('/Users/mezzatab/FN4X/ShareHolders/ShareHolders.xlsx')
		xl.to_excel(writer,'Sheet1')
#		print(xl)
		writer.save()

	def AddBudget(self, Name, Budget):	
		file = '/Users/mezzatab/FN4X/ShareHolders/ShareHolders.xlsx'
		xl=pd.read_excel(file, sheetname='Sheet1')
		print(xl)
		self.nameList = xl["Share Holders"]
		self.shareList = xl["Share Dist"]
		self.shareMoney = xl["Share Money"]
		L=len(self.shareMoney)
		totBal=0	
		sList=self.nameList[self.nameList==Name].index.tolist()
		if len(sList)==1:
			index=sList[0]
			print(self.nameList[0],"Ahmad", index)
#		xl.filter
			self.shareMoney[index]=self.shareMoney[index]+Budget
			for i in range(L):
				totBal=self.shareMoney[i]+totBal
			for i in range(L):
				self.shareList[i]=1.0*self.shareMoney[i]/totBal

			xl["Share Holders"]=self.nameList
			xl["Share Money"]=self.shareMoney	
			xl["Share Dist"]=self.shareList 
			writer = ExcelWriter('/Users/mezzatab/FN4X/ShareHolders/ShareHolders.xlsx')
			xl.to_excel(writer,'Sheet1')
			writer.save()

		else:
			self.AddPerson(Name,Budget)		
#			return 



a=Update()
a.AddPerson('Parth',300)
a.AddBudget('Molla'	,450)


