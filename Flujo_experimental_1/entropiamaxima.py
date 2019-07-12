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
DATASET_PATH = "../Flujo_experimental_1/dataset.csv"

def limpiasaltolinea(text):
    words = text.replace('\n','')
    return words

def main():
    text_data_headers = []
    archivo1=open("Flujo_experimental_1/listadepalabras.txt",'r')
    archivo2=open("Flujo_experimental_1/resultados.txt",'w')
    print("hola estoy haciendo algo")
    for linea in archivo1.readlines():
        text_data_headers.append(limpiasaltolinea(linea))
    

    text_data = pd.read_csv('Flujo_experimental_1/dataset.csv', names=text_data_headers)
    archivo2.write("Numero de observaciones :: "+ str(len(text_data.index)))
    archivo2.write('\n')
    archivo2.write("Numbero de columnas :: "+ str(len(text_data.columns)))
    archivo2.write('\n')
    #Train , Test data split
    train_x, test_x, train_y, test_y = train_test_split(text_data[text_data_headers[:-1]],
                                                        text_data[text_data_headers[-1]], train_size=0.5)

    print("termine de agendar train")
    # Train multi-classification model with logistic regression
    text_data2=text_data.iloc[:,:-1]
    #numero de 1
    unos=text_data2.values.sum()
    suma=text_data2.size
    #numero de 0
    zeros=suma-unos
    archivo2.write("Numero de unos en la matriz: "+str(unos))
    archivo2.write('\n')
    archivo2.write("Numero de 0 en la matriz: "+str(zeros))
    archivo2.write('\n')
    archivo2.write("Sparse of matrix: "+str((100*zeros/suma)))
    archivo2.write('\n')
    archivo2.write("Density of matrix la matriz: "+str((100*unos/suma)))
    archivo2.write('\n')


    mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(train_x, train_y)
    tn = multilabel_confusion_matrix(test_y, mul_lr.predict(test_x),labels=[0,1,2,3] ).ravel()
    print("termine mul_lr")

    archivo2.write("Resultados para País: \n")
    archivo2.write("tn : "+str(tn[0]))
    archivo2.write(" fp : "+str(tn[1]))
    archivo2.write(" fn : "+str(tn[2]))
    archivo2.write(" tp : "+str(tn[3])+'\n')
    archivo2.write("Resultados para Entretención: \n")
    archivo2.write("tn : "+str(tn[4]))
    archivo2.write(" fp : "+str(tn[5]))
    archivo2.write(" fn : "+str(tn[6]))
    archivo2.write(" tp : "+str(tn[7])+'\n')
    archivo2.write("Resultados para Mundo: \n")
    archivo2.write("tn : "+str(tn[8]))
    archivo2.write(" fp : "+str(tn[9]))
    archivo2.write(" fn : "+str(tn[10]))
    archivo2.write(" tp : "+str(tn[11])+'\n')
    archivo2.write("Resultados para Otros: \n")
    archivo2.write("tn : "+str(tn[12]))
    archivo2.write(" fp : "+str(tn[13]))
    archivo2.write(" fn : "+str(tn[14]))
    archivo2.write(" tp : "+str(tn[15])+'\n')    
    archivo2.write("Multinomial Logistic regression Train Accuracy :: " + str(metrics.accuracy_score(train_y, mul_lr.predict(train_x))))
    archivo2.write('\n')
    archivo2.write("Multinomial Logistic regression Test Accuracy :: " + str(metrics.accuracy_score(test_y, mul_lr.predict(test_x))))
    archivo2.write('\n')
    train_x, test_x, train_y, test_y = train_test_split(text_data[text_data_headers[:-1]],
                                                        text_data[text_data_headers[-1]], train_size=0.5)
    # Train multi-classification model with logistic regression
    text_data=text_data.iloc[:,:-1]
    #numero de 1
    unos=text_data.values.sum()
    suma=text_data.size
    #numero de 0
    zeros=suma-unos
    archivo2.write("Numero de unos en la matriz: "+str(unos))
    archivo2.write('\n')
    archivo2.write("Numero de 0 en la matriz: "+str(zeros))
    archivo2.write('\n')
    archivo2.write("Sparse of matrix: "+str((100*zeros/suma)))
    archivo2.write('\n')
    archivo2.write("Density of matrix la matriz: "+str((100*unos/suma)))
    archivo2.write('\n')
    mul_lr2 = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(train_x, train_y)
    tn = multilabel_confusion_matrix(test_y, mul_lr2.predict(test_x),labels=[0,1,2,3] ).ravel()
    archivo2.write("Resultados para País: \n")
    archivo2.write("tn : "+str(tn[0]))
    archivo2.write(" fp : "+str(tn[1]))
    archivo2.write(" fn : "+str(tn[2]))
    archivo2.write(" tp : "+str(tn[3])+'\n')
    archivo2.write("Resultados para Entretención: \n")
    archivo2.write("tn : "+str(tn[4]))
    archivo2.write(" fp : "+str(tn[5]))
    archivo2.write(" fn : "+str(tn[6]))
    archivo2.write(" tp : "+str(tn[7])+'\n')
    archivo2.write("Resultados para Mundo: \n")
    archivo2.write("tn : "+str(tn[8]))
    archivo2.write(" fp : "+str(tn[9]))
    archivo2.write(" fn : "+str(tn[10]))
    archivo2.write(" tp : "+str(tn[11])+'\n')
    archivo2.write("Resultados para Otros: \n")
    archivo2.write("tn : "+str(tn[12]))
    archivo2.write(" fp : "+str(tn[13]))
    archivo2.write(" fn : "+str(tn[14]))
    archivo2.write(" tp : "+str(tn[15])+'\n')    
    archivo2.write("Multinomial Logistic regression Train Accuracy :: " + str(metrics.accuracy_score(train_y, mul_lr2.predict(train_x))))
    archivo2.write('\n')
    archivo2.write("Multinomial Logistic regression Test Accuracy :: " + str(metrics.accuracy_score(test_y, mul_lr2.predict(test_x))))
    archivo2.write('\n')    


if __name__ == "__main__":
    main()