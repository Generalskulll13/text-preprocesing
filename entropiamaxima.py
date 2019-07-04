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
from sklearn.metrics import multilabel_confusion_matrix
#import plotly.graph_objs as go
#import plotly.plotly as py
#from plotly.graph_objs import *
#py.sign_in('Your_ployly_username', 'API_key')

# Dataset Path
DATASET_PATH = "../dataset.csv"

def tokenize(text):
    words = nltk.word_tokenize(text)
    return words

def main():
    text_data_headers = []
    archivo1=open("listadepalabras.txt",'r')
    archivo2=open("resultados.txt",'w')
    for linea in archivo1.readlines():
        text_data_headers.append(tokenize(linea)[0])

    

    text_data = pd.read_csv('dataset.csv', names=text_data_headers)
    archivo2.write("Numero de observaciones :: "+ str(len(text_data.index)))
    archivo2.write('\n')
    archivo2.write("Numbero de columnas :: "+ str(len(text_data.columns)))
    archivo2.write('\n')
    #Train , Test data split
    train_x, test_x, train_y, test_y = train_test_split(text_data[text_data_headers[:-1]],
                                                        text_data[text_data_headers[-1]], train_size=0.5)
    # Train multi-classification model with logistic regression


    # Train multinomial logistic regression model
    mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(train_x, train_y)
    tn = multilabel_confusion_matrix(test_y, mul_lr.predict(test_x),labels=[0,1,2,3] ).ravel()
    print(test_y)
    print(mul_lr.predict(test_x))
    print(tn)
    archivo2.write("Multinomial Logistic regression Train Accuracy :: " + str(metrics.accuracy_score(train_y, mul_lr.predict(train_x))))
    archivo2.write('\n')
    archivo2.write("Multinomial Logistic regression Test Accuracy :: " + str(metrics.accuracy_score(test_y, mul_lr.predict(test_x))))
    archivo2.write('\n')
    


if __name__ == "__main__":
    main()