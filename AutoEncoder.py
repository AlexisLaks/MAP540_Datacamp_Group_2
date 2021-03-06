#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:27:19 2018

@author: viktormalesevic
"""

#%%


#%%
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from collections import Counter as count
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

#%%
# Importing all comments
data = pd.read_csv('data_scraping.csv', encoding = 'ISO-8859-1', index_col = 0, engine="python")

#%%
# Convert to list for later steps
comments = data['comments'].tolist()
comments = comments[:-68]

#%%
# sample comment to test outputs
#comments = ['I LOVE this phone, my Wife has one..... @wife #waddup. I\'ll be going in-to univErsiTY in 4 days. I won\'t give up until I\'ve won this phone phone phone please ~']

#%% 
# Lets only look at reviews with a rating of 3 and below
#comments = data[data['stars']<=3]['comments'].tolist()

#%%
# Given a list of comments, the function will return a list of tokens with -
# special characters and english stopwords removed. This format is useful -
# for further text analysis.
def tokenize(my_list):
    # Lowercase all characters 
    # (like this the same word will contribute to the same token count)
    comments = [item.lower() for item in my_list]
    # Combine all comments into a single string
    comments = ' '.join(comments)
    # We establish a dictionary of the transformation: characters to replace with a space
    transformation = {a:' ' for a in ['@','/','#','.','\\','!',',','(',')','{','}','[',']','-','~','’','"', '*','?','+', '8', '7', '6']}                                
    comments = comments.translate(str.maketrans(transformation))
    # We also want to remove context words that don't have meaning
    comments = comments.replace('iphone', ' ').replace('samsung', ' ').replace('galaxy', ' ').replace('apple', ' ').replace('plus', ' ').replace(' x ', ' ').replace('’', '').replace("'", '')
    
    # nltk's tokenizer
    tkzer = TweetTokenizer(preserve_case = False, strip_handles = True, reduce_len = True)
    tokens = tkzer.tokenize(comments)
    # set of english stopwords
    english_stopwords = set(stopwords.words('english'))
    # Remove english stopwords
    tokens = [i for i in tokens if i not in english_stopwords]
    
    return tokens

#%%
    




#%%
def tokenList(my_list):
    # Lowercase all characters 
    # (like this the same word will contribute to the same token count)
    comments = [item.lower() for item in my_list]
    # We establish a dictionary of the transformation: characters to replace with a space
    # We also want to remove context words that don't have meaning
    transformation = {a:' ' for a in ['@','/','#','.','\\','!',',','(',')','{','}','[',']','-','~', '*','?','+', '8', '7', '6']}
    transB = {b:'' for b in ['','’','"']}
    comments = [item.translate(str.maketrans(transformation)) for item in comments]
    comments = [item.translate(str.maketrans(transB)) for item in comments]
    comments = [item.replace('iphone', ' ').replace('samsung', ' ').replace('galaxy', ' ').replace('apple', ' ').replace('plus', ' ').replace(' x ', ' ').replace('’', '').replace("'", '') for item in comments]
    
    # nltk's tokenizer
    tkzer = TweetTokenizer(preserve_case = False, strip_handles = True, reduce_len = True)
    tokens = [tkzer.tokenize(item) for item in comments]
    
    tokens = []
    wordnet_lemmatizer = WordNetLemmatizer()
    for idx in range(len(comments)):
        words = ([word for word in comments[idx].split() if word not in stopwords.words('english')])
        for idy in range(len(words)):
            words[idy] = wordnet_lemmatizer.lemmatize(words[idy], pos = 'v')
        
        tokens.append(words)
        print('Tokenizing: ',idx+1, ' / ', len(comments))

    return tokens

# given a list of ordered tokens from a document, the function will return-
# a list of neighbouring groups of size n.
def nGrams(input_list, n):
    return list(zip(*[input_list[i:] for i in range(n)]))

# Returns nGrams from a corpus of tokens
def listGrams(input_list, n):
    output =[]
    for idx in range(len(input_list)):
        temp = nGrams(input_list[idx], n)
        output = output + temp
    return output
#%%
tokens = tokenList(comments)
#%%
#docs = ['why hello there', 'omg hello pony', 'she went there? omg']

vec = CountVectorizer()
X = vec.fit_transform(tokens[1])
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
print(X)

#%%
# We have a list of a list of ordered tokens that we need to find the nGrams of
countMonogram = count(listGrams(tokens, 1))
countBigram = count(listGrams(tokens, 2))
countTrigram = count(listGrams(tokens, 3))
countTetragram = count(listGrams(tokens, 4))

#%%
countMonogram.most_common(30)
#%%
countBigram.most_common(30)
#%%
countTrigram.most_common(30)
#%%
countTetragram.most_common(30)
#%%





#%%
import matplotlib.pyplot as plt

def gramGraph(tokens, n, name, top = 30):
    countGram = count(listGrams(tokens, n))
    test = countGram.most_common(top)
    
    labels = []
    values = []
    indexes = range(len(test))
    for i in indexes:
        labels.append(', '.join(test[i][0]))
        values.append(test[i][1])
    
    fig = plt.gcf()
    fig.set_size_inches(.7*top, 10)
    
    plt.bar(indexes, values, 1)
    plt.xticks(indexes, labels, rotation = 70, ha='right')
    plt.title(name, fontsize = 20)
    
    return fig

#%%





#%%
fig = gramGraph(tokens, 1, 'Top 20 Monograms', 20)
#fig.savefig('Plot Monogram S8 Top 20', bbox_inches = 'tight')

#%%
fig = gramGraph(tokens, 2, 'Top 20 Bigrams', 20)
#fig.savefig('Plot Bigram S8 Top 20', bbox_inches = 'tight')

#%%
fig = gramGraph(tokens, 3, 'Top 20 Trigrams', 20)
#fig.savefig('Plot Trigram S8 Top 20', bbox_inches = 'tight')

#%%
fig = gramGraph(tokens, 4, 'Top 20 Tetragrams', 20)

#%%





#%%
# Token Frequency Sparcity Matrix


#%%

#%%

#%%





















