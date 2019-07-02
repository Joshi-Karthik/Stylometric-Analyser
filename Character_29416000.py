# -*- coding: utf-8 -*-
"""
Created on Fri May 25 
@author: Karthik Joshi
Modified  Sun May 27
"""
import string
import pandas as pd

class CharacterAnalyser:
    #intialising the constructor class with an empty dataframe
    def __init__(self):
        self.char_count_df = pd.DataFrame()
        
    '''The given tokenised list is joined and converted back to list so that it provides individual characters
         '''    
    def analyse_characters(self,token_list):        
        char_tokens=list(''.join(token_list))
        char_list=list(string.punctuation)+list(string.ascii_uppercase)
        count_list=[0]*58
        # Running a loop to count each character 
        for each in char_tokens:
            if each in char_list:
                index=char_list.index(each)
                count_list[index]+=1
        # Normalising the count by diividing it by length of list
        count_list= [x /len(char_tokens)  for x in count_list]
        char_freq=list(zip(char_list,count_list))
        #converting it to dataframe
        self.char_count_df= pd.DataFrame(char_freq,columns=['Char','count'])
        
    def __str__(self):
        #overloading the string to get character count
        char_count=''
        for i, row in self.char_count_df.iterrows():
            char_count += str(str(row)) + ' - ' + str(i*len(self.char_count_df)) + '\n'
        return char_count    
            
        
    
    def get_punctuation_frequency(self):
        character_plist=[]
        count_plist=[]
        #running a loop to extract only punctuation from dataframe created above 
        for i, row in self.char_count_df.iterrows():
            if row['Char'] in list(string.punctuation):
                character_plist.append(row['Char'])
                count_plist.append(row['count'])
        zipped=list(zip(character_plist,count_plist))
        #converting into a dataframe
        punct_freq=pd.DataFrame(zipped,columns=['Punctuation','Frequency'])
        return punct_freq
    #get method to return character count
    def get_char_count(self):
        return self.char_count_df

