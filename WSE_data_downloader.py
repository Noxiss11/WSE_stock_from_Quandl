# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 02:18:24 2018

@author: PC1
"""

import quandl
import pandas as pd
import sqlite3
import os
clear=os.system("cls")

#Stocks to download
#companies=["CDPROJEcT","CIGAMES","CCC"]
#company = "CIGAMES"
#Declaration of database
db=sqlite3.connect("GPW.db")
# c=db.cursor()
# db.execute("CREATE TABLE IF NOT EXISTS cigames VALUES(ID INTEGER PRIMARY KEY,Date TEXT,Open REAL,High REAL,Low REAL,Close REAL, PCTChange REAL, Volume REAL, NoOfTrades REAL, Turnover REAL)")

# fiddy_states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(fiddy_states[1][2][1:])
companies = pd.read_html("https://www.gpw.pl/price-archive?show_x=Show+results&type=10&instrument=&date=10-09-2018")
print(companies[1])
print(companies[1]["Name"])
companies =companies[1]["Name"]
# print(companies)
# companies =companies[10:15]
# print(companies)


# def download_data():
 # df = quandl.get("WSE/"+str(company), authtoken="hBFGBDCSpCAyUF4PLiyK")
 # return df
 
#df = download_data()

#print(df)
#print(df["Close"])
# pd.DataFrame.to_sql(df,"CIGAMES",db)
# #########################
count=0
for company in companies:
 clear
 print(company)
 count=count+1
 print(int(count/len(companies)*100) *"|" + str((count/len(companies))*100))
 
 try:
  df = quandl.get("WSE/"+str(company), authtoken="hBFGBDCSpCAyUF4PLiyK")
  pd.DataFrame.to_sql(df,company,db)
 except:
  print("There was a problem with downloading data for " + str(company))
  
 
 
db.close()
# ##############################
# # for company in companies:
 
 # df = quandl.get("WSE/"+str(company), authtoken="hBFGBDCSpCAyUF4PLiyK")
 # print("WSE/"+str(company))
# print("WSE/"+str(company))
# df = quandl.get("WSE/"+str(company), authtoken="hBFGBDCSpCAyUF4PLiyK")
#df.to_csv(str(company)+".csv")