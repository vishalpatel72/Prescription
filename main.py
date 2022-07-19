# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zydNtx7GWZcNz2COQnQ5t0HDlj0z5Hzk
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pandas as pd
import schedule
import time

import gspread
import json
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("data.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread

sheet = file.open("master")  #open sheet
sheet = sheet.sheet1  #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1

rows = sheet.get_all_values()
#print(rows)

df = pd.DataFrame.from_records(rows)
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
df

import numpy as np

df_non = df[df['allopathy/not']=='']


df_non_green = df_non[df_non['Blaze']=='GREEN']

lst = df_non_green.to_numpy().tolist()
headers = df_non_green.columns.tolist()

data = [headers] + lst

sheet = file.open("NonAllopathy_Green") 
sheet = sheet.sheet1 


sheet.update(None, data)

df_non_red = df_non[df_non['Blaze']=='RED']
lst1 = df_non_red.to_numpy().tolist()
headers1 = df_non_red.columns.tolist()
data1 = [headers1] + lst1

sheet = file.open("NonAllopathy_Red") 
sheet = sheet.sheet1 


sheet.update(None, data1)

df_allo = df[df['allopathy/not']=='Allopathy']

lst2 = df_allo.to_numpy().tolist()
headers2 = df_allo.columns.tolist()
data2 = [headers2] + lst2

sheet = file.open("Allopathy") 
sheet = sheet.sheet1 



sheet.update(None, data2)

df_non_green_packed = df_non_green[df_non_green['Operations']=='Packed']
df_allo_packed = df_allo[df_allo['Operations']=='Packed']
df_non_red_packed = df_non_red[df_non_red['Operations']=='Packed']

result = [df_non_green_packed , df_allo_packed , df_non_red_packed]

df_packed = pd.concat(result)
df_packed.drop(df_packed[df_packed['Confirmed'] == 'Cancelled'].index, inplace = True)

lst3 = df_packed.to_numpy().tolist()
headers3 = df_packed.columns.tolist()
data3 = [headers3] + lst3

sheet = file.open("Warehouse") 
sheet = sheet.sheet1 

#worksheet_non_green = gc.open_by_key('https://docs.google.com/spreadsheets/d/18lJ-j8E3jb3ktTXWIEiV9E74-P6xBYTyJhjo0DwipMQ/edit#gid=478417104').sheet1

sheet.update(None, data3)

df_non_green_cancelled = df_non_green[df_non_green['Confirmed']=='Cancelled']
df_allo_cancelled = df_allo[df_allo['Confirmed']== 'Cancelled']
df_non_red_cancelled = df_non_red[df_non_red['Confirmed']=='Cancelled']
df_confirmation_cancelled = df[df['Confirmed']=='Cancelled']

res = [df_non_green_cancelled , df_allo_cancelled , df_non_red_cancelled]

df_cancelled = pd.concat(res)

lst4 = df_cancelled.to_numpy().tolist()
headers4 = df_cancelled.columns.tolist()
data4 = [headers4] + lst4

sheet = file.open("Cancelled") 
sheet = sheet.sheet1 

#worksheet_non_green = gc.open_by_key('https://docs.google.com/spreadsheets/d/18lJ-j8E3jb3ktTXWIEiV9E74-P6xBYTyJhjo0DwipMQ/edit#gid=478417104').sheet1

sheet.update(None, data4)

def update_nonallo_green():
  sheet = file.open("NonAllopathy_Green")  #open sheet
  sheet = sheet.sheet1 
  rows = sheet.get_all_values()
  df_non_green = pd.DataFrame.from_records(rows)
  new_header = df_non_green.iloc[0] #grab the first row for the header
  df_non_green = df_non_green[1:] #take the data less the header row
  df_non_green.columns = new_header #set the header row as the df header
  df_non_green

def update_nonallo_red():
  sheet = file.open("NonAllopathy_Red")  #open sheet
  sheet = sheet.sheet1  #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1

  rows = sheet.get_all_values()
  #print(rows)

  df_non_red = pd.DataFrame.from_records(rows)
  new_header = df_non_red.iloc[0] #grab the first row for the header
  df_non_red = df_non_red[1:] #take the data less the header row
  df_non_red.columns = new_header #set the header row as the df header
  df_non_red

def update_allo():
  sheet = file.open("Allopathy")  #open sheet
  sheet = sheet.sheet1  #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1

  rows = sheet.get_all_values()
  #print(rows)

  df_allo = pd.DataFrame.from_records(rows)
  new_header = df_allo.iloc[0] #grab the first row for the header
  df_allo = df_allo[1:] #take the data less the header row
  df_allo.columns = new_header #set the header row as the df header
  df_allo

def update_master():
  result = [df_non_green , df_non_red , df_allo]
  df= pd.concat(result)

  lst = df.to_numpy().tolist()
  headers = df.columns.tolist()

  data = [headers] + lst
  #print(data)

  sheet = file.open("master") 
  sheet = sheet.sheet1 


  sheet.update(None, data)

def update_warehouse():
  df_non_green_packed = df_non_green[df_non_green['Operations']=='Packed']
  df_allo_packed = df_allo[df_allo['Operations']=='Packed']
  df_non_red_packed = df_non_red[df_non_red['Operations']=='Packed']

  result = [df_non_green_packed , df_allo_packed , df_non_red_packed]

  df_packed = pd.concat(result)
  df_packed.drop(df_packed[df_packed['Confirmed'] == 'Cancelled'].index, inplace = True)

  lst3 = df_packed.to_numpy().tolist()
  headers3 = df_packed.columns.tolist()
  data3 = [headers3] + lst3

  sheet = file.open("Warehouse") 
  sheet = sheet.sheet1 

  #worksheet_non_green = gc.open_by_key('https://docs.google.com/spreadsheets/d/18lJ-j8E3jb3ktTXWIEiV9E74-P6xBYTyJhjo0DwipMQ/edit#gid=478417104').sheet1

  sheet.update(None, data3)

def update_cancelled():
  df_non_green_cancelled = df_non_green[df_non_green['Confirmed']=='Cancelled']
  df_allo_cancelled = df_allo[df_allo['Confirmed']== 'Cancelled']
  df_non_red_cancelled = df_non_red[df_non_red['Confirmed']=='Cancelled']
  df_confirmation_cancelled = df[df['Confirmed']=='Cancelled']

  res = [df_non_green_cancelled , df_allo_cancelled , df_non_red_cancelled]

  df_cancelled = pd.concat(res)

  lst4 = df_cancelled.to_numpy().tolist()
  headers4 = df_cancelled.columns.tolist()
  data4 = [headers4] + lst4

  sheet = file.open("Cancelled") 
  sheet = sheet.sheet1 


  sheet.update(None, data4)

schedule.every(4).seconds.do(update_nonallo_green)
schedule.every(4).seconds.do(update_nonallo_red)
schedule.every(4).seconds.do(update_allo)
schedule.every(4).seconds.do(update_master)
schedule.every(4).seconds.do(update_warehouse)
schedule.every(4).seconds.do(update_cancelled)

while True:
  schedule.run_pending()
  time.sleep(1)
