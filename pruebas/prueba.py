#!/usr/bin/env python
# multinomial_logistic_regression.py
# Author : Saimadhu Polamuri
# Date: 05-May-2017
# About: Multinomial logistic regression model implementation

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split
import nltk
from nltk import word_tokenize, sent_tokenize
def tokenize(text):
    words = nltk.word_tokenize(text)
    return words

def main():
    glass_data_headers = ["Id"]
    archivo1=open("listadepalabras.txt",'r')
    for linea in archivo1.readlines():
        glass_data_headers.append(tokenize(linea)[0])

    print(str(glass_data_headers))

    glass_data = pd.read_csv('dataset.csv', names=glass_data_headers)

    print ("Number of observations :: "+ str(len(glass_data.index)))
    print ("Number of columns :: "+ str(len(glass_data.columns)))
    print ("Headers :: "+ str(glass_data.columns.values))
    print ("Target :: "+ str(glass_data[glass_data_headers[-1]]))
 
if __name__ == "__main__":
    main()