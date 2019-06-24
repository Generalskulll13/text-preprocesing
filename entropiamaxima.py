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
#import plotly.graph_objs as go
#import plotly.plotly as py
#from plotly.graph_objs import *
#py.sign_in('Your_ployly_username', 'API_key')

# Dataset Path
DATASET_PATH = "../dataset.csv"


#def scatter_with_color_dimension_graph(feature, target, layout_labels):
    
#    Scatter with color dimension graph to visualize the density of the
#    Given feature with target
#    :param feature:
#    :param target:
#    :param layout_labels:
#    :return:
    
#    trace1 = go.Scatter(
#        y=feature,
#        mode='markers',
#        marker=dict(
#            size='16',
#            color=target,
#            colorscale='Viridis',
#            showscale=True
#        )
#    )
#    layout = go.Layout(
#        title=layout_labels[2],
#        xaxis=dict(title=layout_labels[0]), yaxis=dict(title=layout_labels[1]))
#    data = [trace1]
#    fig = Figure(data=data, layout=layout)
#    # plot_url = py.plot(fig)
 #   py.image.save_as(fig, filename=layout_labels[1] + '_Density.png')


#def create_density_graph(dataset, features_header, target_header):
#    
#    Create density graph for each feature with target
#    :param dataset:
#    :param features_header:
#    :param target_header:
#    :return:
#        for feature_header in features_header:
#        print "Creating density graph for feature:: {} ".format(feature_header)
#        layout_headers = ["Number of Observation", feature_header + " & " + target_header,
#                          feature_header + " & " + target_header + " Density Graph"]
#        scatter_with_color_dimension_graph(dataset[feature_header], dataset[target_header], layout_headers)
def tokenize(text):
    words = nltk.word_tokenize(text)
    return words

def main():
    glass_data_headers = []
    archivo1=open("listadepalabras.txt",'r')
    for linea in archivo1.readlines():
        glass_data_headers.append(tokenize(linea)[0])

    

    glass_data = pd.read_csv('dataset.csv', names=glass_data_headers)

    print ("Number of observations :: "+ str(len(glass_data.index)))
    print ("Number of columns :: "+ str(len(glass_data.columns)))
    print ("Headers :: "+ str(glass_data.columns.values))
    print ("Target :: "+ str(glass_data[glass_data_headers[-1]]))
    #Train , Test data split

   # print ("glass_data_RI :: "+ str(list(glass_data["amor"][:10])))
   # print ("glass_data_target :: "+ str(np.array([1, 1, 1, 2, 2, 3, 4, 5, 6, 7])))
   # graph_labels = ["Number of Observations", "RI & Glass Type", "Sample RI - Glass Type Density Graph"]
    # scatter_with_color_dimension_graph(list(glass_data["RI"][:10]),
    #                                    np.array([1, 1, 1, 2, 2, 3, 4, 5, 6, 7]), graph_labels)

    # print "glass_data_headers[:-1] :: ", glass_data_headers[:-1]
    # print "glass_data_headers[-1] :: ", glass_data_headers[-1]
    # create_density_graph(glass_data, glass_data_headers[1:-1], glass_data_headers[-1])

    train_x, test_x, train_y, test_y = train_test_split(glass_data[glass_data_headers[:-1]],
                                                        glass_data[glass_data_headers[-1]], train_size=0.7)
    # Train multi-classification model with logistic regression
    lr = linear_model.LogisticRegression()
    lr.fit(train_x, train_y)

    # Train multinomial logistic regression model
    mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(train_x, train_y)

    print ("Logistic regression Train Accuracy :: " + str( metrics.accuracy_score(train_y, lr.predict(train_x))))
    print ("Logistic regression Test Accuracy :: " + str(metrics.accuracy_score(test_y, lr.predict(test_x))))

    print ("Multinomial Logistic regression Train Accuracy :: " + str(metrics.accuracy_score(train_y, mul_lr.predict(train_x))))
    print ("Multinomial Logistic regression Test Accuracy :: " + str(metrics.accuracy_score(test_y, mul_lr.predict(test_x))))


if __name__ == "__main__":
    main()