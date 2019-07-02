# -*- coding: utf-8 -*-
"""
Created on Fri May 25 
@author: Karthik Joshi
Modified  Sun May 27
"""
# Importing all the classes

from preprocessor_29416000 import Preprocessor
from Character_29416000 import CharacterAnalyser
from word_29416000 import WordAnalyser
from visualizer_29416000 import AnalysisVisualiser
import pandas as pd

# Function is defined to read the give  file 
def read_input(file):
    try:
        file_open=open(file,'r')
        return file_open
    except IOError:        
        pass
# Function is defined to do all the analysis for a given author
def all_analyzer(author_token_list):
    char_analyzer=CharacterAnalyser()
    char_analyzer.analyse_characters(author_token_list)
    char_freq=char_analyzer.get_char_count()
    punct_freq=char_analyzer.get_punctuation_frequency()
    word_analyser=WordAnalyser()    
    word_analyser.analyse_words(author_token_list)
    stop_freq=word_analyser.get_stopword_frequency()
    length_freq=word_analyser.get_word_length_frequency()
    author_1=pd.concat(dict(char_freq=char_freq,punct_freq=punct_freq,
                                  stop_freq=stop_freq,length_freq=length_freq),axis=1)
    return author_1


''' Function prompts the user to input files names one by one. If incorrect file name, it throws an error 
    'file not found'. This repeates for the disputed files  '''
def main(): 
    
    # used for output presentation 
    out_list=['Correct files','Disputed files']
    for each in out_list:   
        print('Enter the',each)
        print('-----------------------------------------------------------------------')
        input_file=[]
        files=''
        fopen=''
       #loop to input multiple files
        while files!='quit':
           files=input("Enter the file names of the author and quit to finish" )
           if files!='quit':
               #exception handling
               try:
                   fopen=open(files,'r')
                   input_file.append(files)
               except IOError:
                    print("File not found")
                    pass
    
        Marlowe_list=[] 
        Shakespeare_list=[]               
        # Finding if the file name contains Marlowe or Shankespeare. 
        # Accordingly splitting it based on authors and concatenating into one file 
        for each in input_file:
            find_Marlowe=int(each.find('Marlowe'))
            find_Shakespeare=int(each.find('Shakespeare'))
            if find_Marlowe>-1:        
                Marlowe=read_input(each)
                processor=Preprocessor()
                processor.tokenise(Marlowe)
                Marlowe_list+=processor.get_tokenised_list()
            elif find_Shakespeare>-1:
                Shakespeare=read_input(each)
                processor=Preprocessor()
                processor.tokenise(Shakespeare)
                Shakespeare_list+=processor.get_tokenised_list()
        
        # Checking for length of tokenised list and make sure there are Marlowe and Shakespeare files
        if len(Shakespeare_list)>0 and len(Marlowe_list)>0:
            # two function calls for each author
            author_Marlowe=all_analyzer(Marlowe_list)
            author_Shakespeare=all_analyzer(Shakespeare_list)
            #concatenating two authors to a single dataframe
            all_stats=pd.concat(dict(author_Shakespeare=author_Shakespeare,
                                 author_Marlowe=author_Marlowe),axis=1)
            # exporting it to csv
            all_stats.to_csv('C:/Users/user/Desktop/All_Statistics.csv')
            # Displaying all visual analysis
            analysis=AnalysisVisualiser(all_stats)
            analysis.visualise_character_frequency()
            analysis.visualise_punctuation_frequency()
            analysis.visualise_word_length_frequency()
            analysis.visualise_stopword_frequency()
        # checking if it has only Shakespeare files    
        elif len(Shakespeare_list)>0:
            author_Shakespeare=all_analyzer(Shakespeare_list)
            all_stats=author_Shakespeare
            all_stats.to_csv('C:/Users/user/Desktop/All_Statistics_Shake.csv')
            analysis=AnalysisVisualiser(all_stats)
            analysis.visualise_character_frequency()
            analysis.visualise_punctuation_frequency()
            analysis.visualise_word_length_frequency()
            analysis.visualise_stopword_frequency()
        # checking if has only Marlowe files
        elif len(Marlowe_list)>0:
            author_Marlowe=all_analyzer(Marlowe_list)
            all_stats=author_Marlowe
            all_stats.to_csv('C:/Users/user/Desktop/All_Statistics_Marlowe.csv')
            analysis=AnalysisVisualiser(all_stats)
            analysis.visualise_character_frequency()
            analysis.visualise_punctuation_frequency()
            analysis.visualise_word_length_frequency()
            analysis.visualise_stopword_frequency()
        
if __name__ == "__main__":
    main()

