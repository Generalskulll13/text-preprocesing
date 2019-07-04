import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split
import nltk
from nltk import word_tokenize, sent_tokenize
def main():
    # Glass dataset headers
    glass_data_headers = ["Id", "RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe", "glass-type"]
    # Loading the Glass dataset in to Pandas dataframe 
    glass_data = pd.read_csv('glass.txt', names=glass_data_headers)
 
    print ("Number of observations :: "+ str(len(glass_data.index)))
    print ("Number of columns :: "+ str(len(glass_data.columns)))
    print ("Headers :: "+ str(glass_data.columns.values))
 
if __name__ == "__main__":
    main()