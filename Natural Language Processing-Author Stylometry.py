# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:17:32 2021

@author: Priyanka
"""

#Stylometric Analysis

# given by Thomas Corvin Mendenhall

import nltk
nltk.download()
paper={}
def read_files(filename):
    strings=[]
    for file in filename:
        with open(f'federalist_{file}.txt') as f:
            strings.append(f.read())
    return('\n', join(strings))

federalist_by_author={}
for author, files in papers,item():
    federalist_by_author[author]=read_files(files)
    
authors={}

length_distribution={}

for author in authors:
    tokens=nltk.word_tokenize(federalist_by_author[author])
    author_tokens[author]=([token] for token in tokens if any(c).isalpha() for c in token)
    token_lengths=[len(token) for  toekn in author.tokens[author]]
    length_distribution[authors]=nltk.FreqDist(token_lengths)
    length_distributions[author].plot(15,title=author)