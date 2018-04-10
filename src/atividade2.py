#!/usr/bin/python

# -*- coding: utf-8 -*-
import csv
from sklearn.neighbors import KNeighborsClassifier

def main():
    dataset = csv.reader(open('data/alturapeso.csv'))

    #
    # see: http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
    x = []
    y = []
    for line in dataset:
        x.append([ float(line[0]), float(line[1]) ])
        y.append(int(line[2]))

    f = fit(x, y)

    predict(f)

def fit(x, y):
    neigh = KNeighborsClassifier()
    neigh.fit(x, y)
    return neigh

def predict(neigh):
    print "Predicao para 1,60 de altura e 50Kg de peso"
    print neigh.predict([[1.60, 50]])
    print "Predicao para 1,89 de altura e 102Kg de peso"
    print neigh.predict([[1.89, 102]])
    print "Predicao para 1,75 de altura e 55Kg de peso"
    print neigh.predict([[1.75, 55]])

if __name__ == '__main__':
    main()