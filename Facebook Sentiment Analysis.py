# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:45:17 2021

@author: DELL
"""
#pandas library provides easy to use data structures for data analysis
#Here it helps to convert the excelsheet to dataframe with the help of pandas.
#dataframe: A dataframe is a 2-dimensional structure in the form of a table.
import pandas as pd

#nltk library which is used to process human language
#It also provides sentiment analysis of human data.
#Sentiment analysis involves working out whether a piece of text is positive, negative or neutral.
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#We will use VADAR
#VADAR is the Valence Aware Dictionary and Sentiment Reasoner.
#It also takes into account the intensity of the sentiments.
#Download VADAR lexicon
#lexicon acts as a dictionary here.
nltk.downloader.download('vader_lexicon')

file='Book1.xlsx'

xl=pd.ExcelFile(file)#Read from excel
dfs=xl.parse(xl.sheet_names[0])#data is in first column . Parsing Excelsheet to dataframe

dfs=list(dfs['A'])#name of the column. #remove the blank rows from the data frame.

print(dfs)

sid=SentimentIntensityAnalyzer()

str1="UTC+5:30"

for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k, ss[k])#k=sentiment, ss[k]=intensity of sentiment


