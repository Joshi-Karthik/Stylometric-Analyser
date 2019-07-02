# -*- coding: utf-8 -*-
"""
Created on Fri May 25 
@author: Karthik Joshi
Modified  Sun May 27
"""


import string
import pandas as pd
import numpy as np
#
class WordAnalyser:
    #intialising the constructor class with an empty dataframe
    def __init__(self):
        self.word_count_df=pd.DataFrame()
        
    #overloading the string to print word count without normalization.
    def __str__(self):
        word_count=''
        for i, row in self.word_count_df.iterrows():
            word_count += str(str(row)) + ' - ' + str(i*len(self.word_count_df)) + '\n'
        return word_count
    
    # removes all punctuation and digits and counts only words.
    def analyse_words(self, tokenised_list):
        remove_list=list(string.digits)+list(string.punctuation)
        clean_token=[]
        #running a loop to filter only words
        for i in range(len(tokenised_list)):
           if tokenised_list[i] not in remove_list:
               clean_token.append(tokenised_list[i])        
        # creating a numpy array which will be hepfull to get unique counts of words
        array_tokens=np.array(clean_token) 
        word,count=np.unique(array_tokens, return_counts=True) 
        # normalizing
        count= [x /len(tokenised_list)  for x in count]
        wordcount_list=list(zip(word,count))
        #converting into dataframe
        self.word_count_df= pd.DataFrame(wordcount_list,columns=['Word','Count'])
    
    # Cosidersing only stopwords from words list  
    def get_stopword_frequency(self):
        stopword_open=open('Stopwords_list1.txt','r')
        stopword_list=stopword_open.read().upper().split()
        words_list=[]
        count_list=[]    
        #running a loop to get stopwords and count from the big word list
        for i,row in self.word_count_df.iterrows(): # i stores index, row-stores columns
            if row['Word'] in stopword_list:
                words_list.append(row['Word'])
                count_list.append(row['Count'])
        ''' As the plot should have same number of elements on x-axis, 
        Considering all stopwords even if its not present in the big list of words. 
        Appending Zero if not present'''
        difference_list=list(set(stopword_list)-set(words_list))
        if len(difference_list)!='0':
            words_list=words_list+difference_list
            count_list=count_list+[0]*len(difference_list)       
        zipped=list(zip(words_list,count_list))
        #Converting to a dataframe and returning.
        stopword_freq=pd.DataFrame(zipped,columns=['Word','Count'])
        return stopword_freq
    #Provides word_length frequency of the big word list
    def get_word_length_frequency(self):
        lengths_list=[]   
        # Assuming maximum word length to be 30 to make the x-axis uniform
        assumed_length=[x for x in range(1,30)]
        # calculting the length of each word
        for i,row in self.word_count_df.iterrows():
            lengths_list.append(len(row['Word']))        
        #Counting each unique element in the length list
        length_array=np.array(lengths_list) 
        length_word,count=np.unique(length_array, return_counts=True) 
        length_word=list(length_word)
        count=list(count)
        # to make uniform x-axis adding elements whichever length is not present and count to zero    
        difference_list=list(set(assumed_length)-set(length_word))        
        if len(difference_list)!='0':
            length_word=length_word+difference_list
            count=count+[0]*len(difference_list)
        length_count_list=list(zip(length_word,count))
        # conveting into dataframe an returning it
        length_word_df= pd.DataFrame(length_count_list,columns=['Word_Lengths','Frequency'])
        return length_word_df
   
