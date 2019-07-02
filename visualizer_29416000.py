# -*- coding: utf-8 -*-
"""
Created on Fri May 25 
@author: Karthik Joshi
Modified  Sun May 27
"""
import string
import pandas as pd
import matplotlib.pyplot as plt


class AnalysisVisualiser:
    #Intialising the constructor class with All texts statistics 
    def __init__(self,all_text_stats):
        self.all_text_stats=all_text_stats
    # Gives visualization of character frequency
    def visualise_character_frequency(self):
        '''Try and except block has been added ensure if mulpitple files of 
        different authors are fed as input'''
        try:
            visualise_char_M=self.all_text_stats['author_Marlowe']['char_freq']
            visualise_char_S=self.all_text_stats['author_Shakespeare']['char_freq'] 
            character_list_M=[]
            count_list_M=[]
            #running a loop extract only characters frequencies of Marlowe 
            for i, row in visualise_char_M.iterrows():
                if row['Char'] in list(string.ascii_uppercase):
                    character_list_M.append(row['Char'])
                    count_list_M.append(row['count'])
            zipped=list(zip(character_list_M,count_list_M))
            #converting into a dataframe 
            char_freq_M=pd.DataFrame(zipped,columns=['Char','M_Frequency'])
            
            character_list_S=[]
            count_list_S=[]
            #running a loop extract only characters frequencies of Shake
            for i, row in visualise_char_S.iterrows():
                if row['Char'] in list(string.ascii_uppercase):
                            character_list_S.append(row['Char'])
                            count_list_S.append(row['count'])
            zipped=list(zip(character_list_S,count_list_S))
            char_freq_S=pd.DataFrame(zipped,columns=['Char','S_Frequency'])
            # Merging two dataframes 
            char_freq=char_freq_M.merge(char_freq_S,left_on='Char', right_on='Char', how='inner') 
            #Plotting the graph and exporting as pdf 
            char_freq.set_index('Char').plot(kind='bar',title='Relative Freqeuncy of Character of Shakespeare and Marlowe')
            plt.savefig('C:/Users/user/Desktop/Character.pdf')            
        except KeyError: 
            pass
        # analysis of the conflict file
        try:
            visualise_char=self.all_text_stats['char_freq']
            character_list=[]
            count_list=[]
            for i, row in visualise_char.iterrows():
                if row['Char'] in list(string.ascii_uppercase):
                    character_list.append(row['Char'])
                    count_list.append(row['count'])
            zipped=list(zip(character_list,count_list))
            char_freq=pd.DataFrame(zipped,columns=['Char','Frequency'])
            char_freq.set_index('Char').plot(kind='bar',title='Relative Freqeuncy of Character')    
            plt.savefig('C:/Users/user/Desktop/Character_individual.pdf')    
        except KeyError:
            pass
            
   #Gives visualization of Punctuation frequency     
    def visualise_punctuation_frequency(self): 
        try:
            visualise_punct_M=self.all_text_stats['author_Marlowe']['punct_freq']
            visualise_punct_S=self.all_text_stats['author_Shakespeare']['punct_freq']        
            punct_list_M=[]
            count_list_M=[]
            #running a loop extract only punctuation frequencies of Marlowe
            for i, row in visualise_punct_M.iterrows():
                if row['Punctuation'] in list(string.punctuation):
                    punct_list_M.append(row['Punctuation'])
                    count_list_M.append(row['Frequency'])
            zipped=list(zip(punct_list_M,count_list_M))
            punct_freq_M=pd.DataFrame(zipped,columns=['Punctuation','M_Frequency'])
            
            punct_list_S=[]
            count_list_S=[]
            #running a loop extract only punctuation frequencies of Shake
            for i, row in visualise_punct_S.iterrows():
                if row['Punctuation'] in list(string.punctuation):
                    punct_list_S.append(row['Punctuation'])
                    count_list_S.append(row['Frequency'])
            zipped=list(zip(punct_list_S,count_list_S))
            punct_freq_S=pd.DataFrame(zipped,columns=['Punctuation','S_Frequency'])
            #Merging and plotting 
            punct_freq=punct_freq_M.merge(punct_freq_S,left_on='Punctuation', right_on='Punctuation', how='inner') 
            punct_freq.set_index('Punctuation').plot(kind='bar',title='Relative Freqeuncy of Punctuation of Shakespeare and Marlowe')
            #exporitng as pdf
            plt.savefig('C:/Users/user/Desktop/punctuation.pdf')
        except KeyError:
            pass
        # analysis of the conflict file
        try:
            visualise_punct=self.all_text_stats['punct_freq']
            punct_list=[]
            count_list=[]
            for i, row in visualise_punct.iterrows():
                if row['Punctuation'] in list(string.punctuation):
                    punct_list.append(row['Punctuation'])
                    count_list.append(row['Frequency'])
            zipped=list(zip(punct_list,count_list))
            punct_freq=pd.DataFrame(zipped,columns=['Punctuation','Frequency'])
            punct_freq.set_index('Punctuation').plot(kind='bar',title='Relative Freqeuncy of Punctuation')
            plt.savefig('C:/Users/user/Desktop/punctuation_individual.pdf')
            
        except KeyError:
            pass
    #Gives visualization of Punctuation frequency     
    def visualise_word_length_frequency(self):
        
        try:
            visualise_word_len_M=self.all_text_stats['author_Marlowe']['length_freq']
            visualise_word_len_S=self.all_text_stats['author_Shakespeare']['length_freq']
            len_list_M=[]
            count_list_M=[]
            #running a loop extract only Word-length frequencies of Marlowe
            for i, row in visualise_word_len_M.iterrows():
                if row['Word_Lengths'] in range(1,30):
                    len_list_M.append(row['Word_Lengths'])
                    count_list_M.append(row['Frequency'])
            zipped=list(zip(len_list_M,count_list_M))
            len_freq_M=pd.DataFrame(zipped,columns=['Lengths','M_Frequency'],index=range(1,30))
                    
            len_list_S=[]
            count_list_S=[]
             #running a loop extract only Word-length frequencies of Shake
            for i, row in visualise_word_len_S.iterrows():
                if row['Word_Lengths'] in range(1,30):
                    len_list_S.append(row['Word_Lengths'])
                    count_list_S.append(row['Frequency'])
            zipped=list(zip(len_list_S,count_list_S))
            len_freq_S=pd.DataFrame(zipped,columns=['Lengths','S_Frequency'],index=range(1,30))
            #Merging and plotting         
            len_freq=len_freq_M.merge(len_freq_S,left_on='Lengths', right_on='Lengths', how='inner') 
            len_freq.set_index('Lengths').plot(kind='bar',title='Relative Freqeuncy of Word Lengths of Shakespeare and Marlowe')
            #Exporting it to pdf
            plt.savefig('C:/Users/user/Desktop/Word_length.pdf')
        except KeyError:
            pass
         # analysis of the conflict file
        try:
            visualise_word_len=self.all_text_stats['length_freq']
            len_list=[]
            count_list=[]
            for i, row in visualise_word_len.iterrows():
                if row['Word_Lengths'] in range(1,30):
                    len_list.append(row['Word_Lengths'])
                    count_list.append(row['Frequency'])
            zipped=list(zip(len_list,count_list))
            len_freq=pd.DataFrame(zipped,columns=['Lengths','Frequency'],index=range(1,30))
            len_freq.set_index('Lengths').plot(kind='bar',title='Relative Freqeuncy of Word Lengths')
            plt.savefig('C:/Users/user/Desktop/Word_length_individual.pdf')
        except KeyError:
            pass
    #Gives visualization of Stop Word frequency             
    def visualise_stopword_frequency(self):
        try:
            visualise_stop_word_M=self.all_text_stats['author_Marlowe']['stop_freq']
            visualise_stop_word_S=self.all_text_stats['author_Shakespeare']['stop_freq']
            # Opening the file stopwords_list1
            stopword_open=open('Stopwords_list1.txt','r')
            # conveting all upper case and list of tokens 
            stopword_list=stopword_open.read().upper().split()
            stop_list_M=[]
            count_list_M=[]
            #running a loop extract only Word-length frequencies of Marlowe
            for i, row in visualise_stop_word_M.iterrows():
                if row['Word'] in stopword_list:
                    stop_list_M.append(row['Word'])
                    count_list_M.append(row['Count'])
            zipped=list(zip(stop_list_M,count_list_M))
            stop_word_freq_M=pd.DataFrame(zipped,columns=['Word','M_Frequency'])
             #running a loop extract only Word-length frequencies of Shake       
            stop_list_S=[]
            count_list_S=[]
            for i, row in visualise_stop_word_S.iterrows():
                if row['Word'] in stopword_list:
                    stop_list_S.append(row['Word'])
                    count_list_S.append(row['Count'])
            zipped=list(zip(stop_list_S,count_list_S))
            stop_word_freq_S=pd.DataFrame(zipped,columns=['Word','S_Frequency'])
            #Merging and plotting only top 30 stopwords        
            stop_word_freq=stop_word_freq_S.merge(stop_word_freq_M,left_on='Word', right_on='Word', how='inner') 
            stop_word_freq.set_index('Word').sort_values(['M_Frequency','S_Frequency'],ascending=False).plot(kind='bar',figsize=(60,20),title='Relative Freqeuncy of Stop Word of Shakespeare and Marlowe')
            # exporting to a pdf
            plt.savefig('C:/Users/user/Desktop/StopWord.pdf')
        except KeyError:
            pass
        # analysis of the conflict file
        try:
            visualise_stop_word=self.all_text_stats['stop_freq']
            stop_list=[]
            count_list=[]
            stopword_open=open('Stopwords_list1.txt','r')
            stopword_list=stopword_open.read().upper().split()
            for i, row in visualise_stop_word.iterrows():
                if row['Word'] in stopword_list:
                    stop_list.append(row['Word'])
                    count_list.append(row['Count'])
            zipped=list(zip(stop_list,count_list))
            stop_word_freq=pd.DataFrame(zipped,columns=['Word','Frequency'])
            stop_word_freq=stop_word_freq.sort_values('Frequency',ascending=False)
            # plotting and exporting the graph
            # zoom in the graph to get clear values on x-axis
            stop_word_freq.set_index('Word').plot(kind='bar',title='Relative Freqeuncy of Stop Word',figsize=(60,20))
            plt.savefig('C:/Users/user/Desktop/StopWord_individual.pdf')
        except KeyError:
            pass
        