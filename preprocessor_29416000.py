# -*- coding: utf-8 -*-
"""
Created on Fri May 25 
@author: Karthik Joshi
Modified  Sun May 27
"""
''' This class tokenises any .tok file given as a input'''
class Preprocessor:
    #intialising the constructor class with an empty list
    def __init__(self):
        self.token_list=[]
    ''' Cleaning the file belore converting into list using string operations. 
    Converting all lowercase characters to uppercase for simplicity'''    
    def tokenise(self,input_sequence):
        self.token_list=input_sequence.read().upper().split()
        
    # overloading the string method to give length of the token_list    
    def __str__(self):
        return str(len(self.token_list))
    # get method used to retun token_list
    def get_tokenised_list(self):
        return self.token_list
